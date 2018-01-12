from __future__ import absolute_import

import ctypes
import base64
import requests

from struct import pack, unpack

from pgoapi.exceptions import BadHashRequestException, HashingOfflineException, HashingQuotaExceededException, HashingTimeoutException, MalformedHashResponseException, NoHashKeyException, TempHashingBanException, UnexpectedHashResponseException


class HashServer:
    _session = requests.session()
    _adapter = requests.adapters.HTTPAdapter(pool_maxsize=500, pool_block=True)
    _session.mount('http://', _adapter)
    _session.mount('https://', _adapter)
    _session.verify = True
    _endpoint = 'https://pokehash.buddyauth.com/api/v157_5/hash'
    _headers = {
        'User-Agent': 'Python pgoapi @pogodev',
        'content-type': 'application/json',
        'Accept': 'application/json',
        'X-MaxRPMCount': '32000'
    }

    @staticmethod
    def hash(timestamp, latitude, longitude, accuracy, authticket,
             sessiondata, requestslist, token):

        if not token:
            raise NoHashKeyException('Token not provided for hashing server.')

        headers = HashServer._headers.copy()
        headers['X-AuthToken'] = token

        payload = {
            'Timestamp':
            timestamp,
            'Latitude64':
            unpack('<q', pack('<d', latitude))[0],
            'Longitude64':
            unpack('<q', pack('<d', longitude))[0],
            'Accuracy64':
            unpack('<q', pack('<d', accuracy))[0],
            'AuthTicket':
            base64.b64encode(authticket).decode('ascii'),
            'SessionData':
            base64.b64encode(sessiondata).decode('ascii'),
            'Requests': [
                base64.b64encode(x.SerializeToString()).decode('ascii')
                for x in requestslist
            ]
        }

        # request hashes from hashing server
        try:
            response = HashServer._session.post(
                HashServer._endpoint, json=payload, headers=headers, timeout=30)
        except requests.exceptions.Timeout:
            raise HashingTimeoutException('Hashing request timed out.')
        except requests.exceptions.ConnectionError as error:
            raise HashingOfflineException(error)

        if response.status_code == 400:
            raise BadHashRequestException(
                "400: Bad request, error: {}".format(response.text))
        elif response.status_code == 403:
            raise TempHashingBanException(
                'Your IP was temporarily banned for sending too many requests with invalid keys'
            )
        elif response.status_code == 429:
            raise HashingQuotaExceededException(
                "429: Request limited, error: {}".format(response.text))
        elif response.status_code in (502, 503, 504):
            raise HashingOfflineException(
                '{} Server Error'.format(response.status_code))
        elif response.status_code != 200:
            error = 'Unexpected HTTP server response - needs 200 got {c}. {t}'.format(
                c=response.status_code, t=response.text)
            raise UnexpectedHashResponseException(error)

        if not response.content:
            raise MalformedHashResponseException('Response was empty')

        try:
            response_parsed = response.json()
        except ValueError:
            raise MalformedHashResponseException(
                'Unable to parse JSON from hash server.')

        location_auth_hash = ctypes.c_int32(
            response_parsed['locationAuthHash']).value
        location_hash = ctypes.c_int32(
            response_parsed['locationHash']).value

        request_hashes = []
        for request_hash in response_parsed['requestHashes']:
            request_hashes.append(ctypes.c_uint64(request_hash).value)

        return (location_hash, location_auth_hash, request_hashes, response.headers)
