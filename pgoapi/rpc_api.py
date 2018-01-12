"""
pgoapi - Pokemon Go API
Copyright (c) 2016 tjado <https://github.com/tejado>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.

Author: tjado <https://github.com/tejado>
"""

from __future__ import absolute_import

import os
import random
import logging
import requests
import subprocess

from importlib import import_module

from google.protobuf import message
from pycrypt import pycrypt

from pgoapi.exceptions import (AuthTokenExpiredException, BadRequestException, MalformedNianticResponseException, NianticIPBannedException, NianticOfflineException, NianticThrottlingException, NianticTimeoutException, NotLoggedInException, ServerApiEndpointRedirectException, UnexpectedResponseException)
from pgoapi.utilities import to_camel_case, get_time, weighted_choice
from pgoapi.hash_server import HashServer

from . import protos
from pogoprotos.networking.envelopes.request_envelope_pb2 import RequestEnvelope
from pogoprotos.networking.envelopes.response_envelope_pb2 import ResponseEnvelope
from pogoprotos.networking.requests.request_type_pb2 import RequestType
from pogoprotos.networking.platform.platform_request_type_pb2 import PlatformRequestType
from pogoprotos.networking.envelopes.signature_pb2 import Signature
from pogoprotos.networking.platform.requests.send_encrypted_signature_request_pb2 import SendEncryptedSignatureRequest
from pogoprotos.networking.platform.requests.unknown_ptr8_request_pb2 import UnknownPtr8Request


class RpcApi:
    log = logging.getLogger(__name__)
    _session = None

    @staticmethod
    def create_session():
        session = requests.session()
        adapter = requests.adapters.HTTPAdapter(pool_maxsize=150, pool_block=True)
        # proxies use the adapter by it's own url not endpoint so all 3 are needed
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        session.mount('socks5://', adapter)

        # requests' Session calls .default_headers() in init, which
        # makes it set a bunch of default headers, including
        # 'Connection': 'keep-alive', so we overwrite all of them.
        session.headers = {
            'User-Agent': 'Niantic App',
            'Content-Type': 'application/binary',
            'Accept-Encoding': 'identity, gzip'
        }
        session.verify = True
        return session

    @staticmethod
    def get_session(state):
        if state.session:
            return state.session
        if not RpcApi._session:
            RpcApi._session = RpcApi.create_session()
        return RpcApi._session

    @staticmethod
    def decode_raw(raw):
        output = error = None
        try:
            process = subprocess.Popen(
                ['protoc', '--decode_raw'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                close_fds=True)
            output, error = process.communicate(raw)
        except (subprocess.SubprocessError, OSError):
            output = "Couldn't find protoc in your environment OR other issue..."

        return output

    @staticmethod
    def get_class(cls):
        module_, class_ = cls.rsplit('.', 1)
        class_ = getattr(import_module(module_), to_camel_case(class_))
        return class_

    @staticmethod
    def _make_rpc(endpoint, request_proto_plain, state, proxies):
        RpcApi.log.debug('Execution of RPC')

        request_proto_serialized = request_proto_plain.SerializeToString()
        try:
            # adapter = RpcApi.get_session(state).adapters['https://']
            # RpcApi.log.error(adapter.poolmanager.connection_from_url(endpoint).num_connections)
            http_response = RpcApi.get_session(state).post(
                endpoint, data=request_proto_serialized, timeout=30,
                proxies=proxies)
        except requests.exceptions.Timeout:
            raise NianticTimeoutException('RPC request timed out.')
        except requests.exceptions.ConnectionError as e:
            raise NianticOfflineException(e)

        return http_response

    @staticmethod
    def request(endpoint,
                subrequests,
                platforms,
                player_position,
                state,
                hash_key,
                proxies):

        if not state.auth_provider or state.auth_provider.is_login() is False:
            raise NotLoggedInException()

        (request, hash_headers) = RpcApi._build_main_request(
            subrequests, platforms, player_position, state, hash_key)
        response = RpcApi._make_rpc(endpoint, request, state, proxies)

        response_dict = RpcApi._parse_main_response(response, subrequests)

        # some response validations
        status_code = response_dict['envelope'].status_code
        ticket = response_dict['envelope'].auth_ticket
        if ticket:
            state.auth_provider.check_authentication(
                ticket.expire_timestamp_ms, ticket.start, ticket.end)

        if status_code == 102:
            raise AuthTokenExpiredException
        elif status_code == 52:
            raise NianticThrottlingException(
                "Request throttled by server... slow down man")
        elif status_code == 53:
            api_url = response_dict.get('api_url')
            if api_url:
                exception = ServerApiEndpointRedirectException()
                exception.set_redirected_endpoint(api_url)
                raise exception
            else:
                raise UnexpectedResponseException

        # add hash headers
        response_dict['hash_headers'] = hash_headers
        return response_dict

    @staticmethod
    def _build_main_request(subrequests,
                            platforms,
                            player_position,
                            state,
                            hash_key):
        RpcApi.log.debug('Generating main RPC request...')

        request = RequestEnvelope()
        request.status_code = 2
        request.request_id = state.get_next_request_id()
        RpcApi.log.debug('RPC Request ID: %s.', request.request_id)
        # 5: 43%, 10: 30%, 30: 5%, 50: 4%, 65: 10%, 200: 1%, float: 7%
        request.accuracy = weighted_choice([
            (5, 43),
            (10, 30),
            (30, 5),
            (50, 4),
            (65, 10),
            (200, 1),
            (random.uniform(65, 200), 7)
        ])

        if player_position:
            request.latitude, request.longitude, altitude = player_position

        # generate sub requests before Signature generation
        request = RpcApi._build_sub_requests(request, subrequests)
        request = RpcApi._build_platform_requests(request, platforms)

        ticket = state.auth_provider.get_ticket()
        if ticket:
            RpcApi.log.debug(
                'Found Session Ticket - using this instead of oauth token')
            request.auth_ticket.expire_timestamp_ms, request.auth_ticket.start, request.auth_ticket.end = ticket
            ticket_serialized = request.auth_ticket.SerializeToString()

        else:
            RpcApi.log.debug(
                'No Session Ticket found - using OAUTH Access Token')
            auth_provider = state.auth_provider
            request.auth_info.provider = auth_provider.get_name()
            request.auth_info.token.contents = auth_provider.get_access_token()
            request.auth_info.token.unknown2 = state.token2
            # Sig uses this when no auth_ticket available.
            ticket_serialized = request.auth_info.SerializeToString()

        sig = Signature()

        sig.session_hash = state.session_hash
        sig.timestamp = get_time(ms=True)
        sig.timestamp_since_start = get_time(ms=True) - state.start_time

        (sig.location_hash2, sig.location_hash1, request_hash, headers) = HashServer.hash(
            sig.timestamp, request.latitude, request.longitude,
            request.accuracy, ticket_serialized, sig.session_hash,
            request.requests, hash_key)
        sig.request_hash.extend(request_hash)

        loc = sig.location_fix.add()
        sen = sig.sensor_info.add()

        sen.timestamp_snapshot = sig.timestamp_since_start - int(random.triangular(93, 4900, 3000))
        loc.timestamp_snapshot = sig.timestamp_since_start - int(random.triangular(320, 3000, 1000))

        loc.provider = 'fused'
        loc.latitude = request.latitude
        loc.longitude = request.longitude

        loc.altitude = altitude or random.uniform(150, 250)

        if random.random() > .85:
            # no reading for roughly 1 in 7 updates
            loc.course = -1
            loc.speed = -1
        else:
            loc.course = state.course
            loc.speed = random.triangular(0.25, 9.7, 8.2)

        loc.provider_status = 3
        loc.location_type = 1
        if isinstance(request.accuracy, float):
            loc.horizontal_accuracy = weighted_choice([
                (request.accuracy, 50),
                (65, 40),
                (200, 10)
            ])
            loc.vertical_accuracy = weighted_choice([
                (random.uniform(10, 96), 50),
                (10, 34),
                (12, 5),
                (16, 3),
                (24, 4),
                (32, 2),
                (48, 1),
                (96, 1)
            ])
        else:
            loc.horizontal_accuracy = request.accuracy
            if request.accuracy >= 10:
                loc.vertical_accuracy = weighted_choice([
                    (6, 4),
                    (8, 34),
                    (10, 35),
                    (12, 11),
                    (16, 4),
                    (24, 8),
                    (32, 3),
                    (48, 1)
                ])
            else:
                loc.vertical_accuracy = weighted_choice([
                    (3, 15),
                    (4, 39),
                    (6, 14),
                    (8, 13),
                    (10, 14),
                    (12, 5)
                ])

        sen.magnetic_field_accuracy = weighted_choice([
            (-1, 8),
            (0, 2),
            (1, 42),
            (2, 48)
        ])
        if sen.magnetic_field_accuracy == -1:
            sen.magnetic_field_x = 0
            sen.magnetic_field_y = 0
            sen.magnetic_field_z = 0
        else:
            sen.magnetic_field_x = state.magnetic_field_x
            sen.magnetic_field_y = state.magnetic_field_y
            sen.magnetic_field_z = state.magnetic_field_z

        sen.linear_acceleration_x = random.triangular(-1.5, 2.5, 0)
        sen.linear_acceleration_y = random.triangular(-1.2, 1.4, 0)
        sen.linear_acceleration_z = random.triangular(-1.4, .9, 0)
        sen.attitude_pitch = random.triangular(-1.56, 1.57, 0.475)
        sen.attitude_yaw = random.triangular(-1.56, 3.14, .1)
        sen.attitude_roll = random.triangular(-3.14, 3.14, 0)
        sen.rotation_rate_x = random.triangular(-3.2, 3.52, 0)
        sen.rotation_rate_y = random.triangular(-3.1, 4.88, 0)
        sen.rotation_rate_z = random.triangular(-6, 3.7, 0)
        sen.gravity_x = random.triangular(-1, 1, 0.01)
        sen.gravity_y = random.triangular(-1, 1, -.4)
        sen.gravity_z = random.triangular(-1, 1, -.4)
        sen.status = 3

        sig.unknown25 = 4500779412463383546
        for key in state.device_info:
            setattr(sig.device_info, key, state.device_info[key])
        sig.activity_status.stationary = True

        signature_proto = sig.SerializeToString()

        if RpcApi._needsPtr8(subrequests):
            plat_eight = UnknownPtr8Request()
            plat_eight.message = '15c79df0558009a4242518d2ab65de2a59e09499'
            plat8 = request.platform_requests.add()
            plat8.type = 8
            plat8.request_message = plat_eight.SerializeToString()

        sig_request = SendEncryptedSignatureRequest()
        sig_request.encrypted_signature = pycrypt(signature_proto,
                                                  sig.timestamp_since_start)
        plat = request.platform_requests.add()
        plat.type = 6
        plat.request_message = sig_request.SerializeToString()

        request.ms_since_last_locationfix = sig.timestamp_since_start - loc.timestamp_snapshot

        RpcApi.log.debug('Generated protobuf request: \n\r%s', request)

        return (request, headers)

    @staticmethod
    def _needsPtr8(requests):
        if len(requests) == 0:
            return False
        randval = random.uniform(0, 1)
        rtype, _ = requests[0]
        # GetMapObjects or GetPlayer: 50%
        # Encounter: 10%
        # Others: 3%
        if ((rtype in (2, 106) and randval > 0.5)
                or (rtype == 102 and randval > 0.9) or randval > 0.97):
            return True
        return False

    @staticmethod
    def _build_sub_requests(mainrequest, subrequest_list):
        RpcApi.log.debug('Generating sub RPC requests...')

        for entry_id, params in subrequest_list:
            if params:
                entry_name = RequestType.Name(entry_id)
                proto_name = entry_name.lower() + '_message'
                bytes = RpcApi._get_proto_bytes(
                    'pogoprotos.networking.requests.messages.', proto_name,
                    params)

                subrequest = mainrequest.requests.add()
                subrequest.request_type = entry_id
                subrequest.request_message = bytes

            else:
                subrequest = mainrequest.requests.add()
                subrequest.request_type = entry_id

        return mainrequest

    @staticmethod
    def _build_platform_requests(mainrequest, platform_list):
        RpcApi.log.debug('Generating platform RPC requests...')

        for entry_id, params in platform_list:
            if params:
                entry_name = PlatformRequestType.Name(entry_id)
                if entry_name == 'UNKNOWN_PTR_8':
                    entry_name = 'UNKNOWN_PTR8'
                proto_name = entry_name.lower() + '_request'
                bytes = RpcApi._get_proto_bytes(
                    'pogoprotos.networking.platform.requests.', proto_name,
                    params)

                platform = mainrequest.platform_requests.add()
                platform.type = entry_id
                platform.request_message = bytes

            else:
                platform = mainrequest.platform_requests.add()
                platform.type = entry_id

        return mainrequest

    @staticmethod
    def _get_proto_bytes(path, name, entry_content):
        proto_classname = path + name + '_pb2.' + name
        proto = RpcApi.get_class(proto_classname)()

        RpcApi.log.debug("Subrequest class: %s", proto_classname)

        for key, value in entry_content.items():
            if isinstance(value, list):
                RpcApi.log.debug("Found list: %s - trying as repeated", key)
                for i in value:
                    try:
                        RpcApi.log.debug("%s -> %s", key, i)
                        r = getattr(proto, key)
                        r.append(i)
                    except Exception as e:
                        RpcApi.log.warning(
                            'Argument %s with value %s unknown inside %s (Exception: %s)',
                            key, i, proto_classname, e)
            elif isinstance(value, dict):
                for k in value.keys():
                    try:
                        r = getattr(proto, key)
                        setattr(r, k, value[k])
                    except Exception as e:
                        RpcApi.log.warning(
                            'Argument %s with value %s unknown inside %s (Exception: %s)',
                            key, str(value), proto_classname, e)
            else:
                try:
                    setattr(proto, key, value)
                except Exception as e:
                    try:
                        RpcApi.log.debug("%s -> %s", key, value)
                        r = getattr(proto, key)
                        r.append(value)
                    except Exception as e:
                        RpcApi.log.warning(
                            'Argument %s with value %s unknown inside %s (Exception: %s)',
                            key, value, proto_classname, e)

        return proto.SerializeToString()

    @staticmethod
    def _parse_main_response(response_raw, subrequests):
        RpcApi.log.debug('Parsing main RPC response...')

        if response_raw.status_code == 400:
            raise BadRequestException("400: Bad Request")
        if response_raw.status_code == 403:
            raise NianticIPBannedException(
                "Seems your IP Address is banned or something else went badly wrong..."
            )
        elif response_raw.status_code in (502, 503, 504):
            raise NianticOfflineException(
                '{} Server Error'.format(response_raw.status_code))
        elif response_raw.status_code != 200:
            error = 'Unexpected HTTP server response - needs 200 got {}'.format(
                response_raw.status_code)
            RpcApi.log.warning(error)
            RpcApi.log.debug('HTTP output: \n%s',
                             response_raw.content.decode('utf-8'))
            raise UnexpectedResponseException(error)

        if not response_raw.content:
            RpcApi.log.warning('Empty server response!')
            raise MalformedNianticResponseException('Empty server response!')

        response_proto = ResponseEnvelope()
        try:
            response_proto.ParseFromString(response_raw.content)
        except message.DecodeError as e:
            RpcApi.log.error('Could not parse response: %s', e)
            raise MalformedNianticResponseException(
                'Could not decode response.')

        RpcApi.log.debug('Protobuf structure of rpc response:\n\r%s',
                         response_proto)
        try:
            RpcApi.log.debug(
                'Decode raw over protoc (protoc has to be in your PATH):\n\r%s',
                RpcApi.decode_raw(response_raw.content).decode('utf-8'))
        except Exception:
            RpcApi.log.debug('Error during protoc parsing - ignored.')

        response_proto_dict = {'envelope': response_proto}

        if not response_proto_dict:
            raise MalformedNianticResponseException(
                'Could not convert protobuf to dict.')

        response_proto_dict = RpcApi._parse_sub_responses(
            response_proto, subrequests, response_proto_dict)

        # It can't be done before.
        del response_proto_dict['envelope'].returns[:]

        return response_proto_dict

    @staticmethod
    def _parse_sub_responses(response_proto,
                             subrequests_list,
                             response_proto_dict):
        RpcApi.log.debug('Parsing sub RPC responses...')
        response_proto_dict['responses'] = {}

        if response_proto.status_code == 53:
            exception = ServerApiEndpointRedirectException()
            exception.set_redirected_endpoint(response_proto.api_url)
            raise exception

        i = 0
        for subresponse in response_proto.returns:
            entry_id, _ = subrequests_list[i]
            entry_name = RequestType.Name(entry_id)
            proto_name = entry_name.lower() + '_response'
            proto_classname = 'pogoprotos.networking.responses.' + proto_name + '_pb2.' + proto_name

            RpcApi.log.debug("Parsing class: %s", proto_classname)

            subresponse_return = None
            try:
                subresponse_extension = RpcApi.get_class(proto_classname)()
            except Exception:
                subresponse_extension = None
                error = 'Protobuf definition for {} not found'.format(
                    proto_classname)
                subresponse_return = error
                RpcApi.log.warning(error)

            if subresponse_extension:
                try:
                    subresponse_extension.ParseFromString(subresponse)
                    subresponse_return = subresponse_extension
                except Exception:
                    error = "Protobuf definition for {} seems not to match".format(
                        proto_classname)
                    subresponse_return = error
                    RpcApi.log.warning(error)

            response_proto_dict['responses'][entry_name] = subresponse_return
            i += 1

        return response_proto_dict


# Original by Noctem.
class RpcState:
    def __init__(self, device_info, auth_provider):
        self.session_hash = os.urandom(16)
        self.mag_x_min = random.uniform(-80, 60)
        self.mag_x_max = self.mag_x_min + 20
        self.mag_y_min = random.uniform(-120, 90)
        self.mag_y_max = self.mag_y_min + 30
        self.mag_z_min = random.uniform(-70, 40)
        self.mag_z_max = self.mag_y_min + 15
        self._course = random.uniform(0, 359.99)
        self.auth_provider = auth_provider

        # data fields for SignalAgglom
        self.token2 = random.randint(1, 59)
        self.course = random.uniform(0, 360)

        self.device_info = device_info

        self.RPC_ID_LOW = 1
        self.RPC_ID_HIGH = 1
        self.start_time = get_time(ms=True) - random.randint(6000, 10000)
        self.session = None

    @property
    def magnetic_field_x(self):
        return random.uniform(self.mag_x_min, self.mag_x_max)

    @property
    def magnetic_field_y(self):
        return random.uniform(self.mag_y_min, self.mag_y_max)

    @property
    def magnetic_field_z(self):
        return random.uniform(self.mag_z_min, self.mag_z_max)

    @property
    def course(self):
        self._course = random.triangular(0, 359.99, self._course)
        return self._course

    def get_next_request_id(self):
        self.RPC_ID_LOW += 1
        self.RPC_ID_HIGH = ((7**5) * self.RPC_ID_HIGH) % ((2**31) - 1)
        reqid = (self.RPC_ID_HIGH << 32) | self.RPC_ID_LOW
        return reqid
