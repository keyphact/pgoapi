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
from future.standard_library import install_aliases

install_aliases()

import requests

from urllib.parse import parse_qs, urlsplit
from six import string_types

from pgoapi.auth import Auth
from pgoapi.utilities import get_time
from pgoapi.exceptions import AuthException, AuthTimeoutException, InvalidCredentialsException

from requests.exceptions import RequestException, Timeout


class AuthPtc(Auth):
    def __init__(self, username=None, password=None, user_agent=None, timeout=None, locale=None):
        Auth.__init__(self)

        self._auth_provider = 'ptc'

        self._session = requests.session()
        self._session.headers = {'User-Agent': user_agent or 'pokemongo/1 CFNetwork/811.4.18 Darwin/16.5.0',
                                 'Host': 'sso.pokemon.com', 'X-Unity-Version': '5.5.1f1'}
        self._username = username
        self._password = password
        self.timeout = timeout or 15
        self.locale = locale or 'en_US'

    def set_proxy(self, proxy_config):
        self._session.proxies = proxy_config

    def user_login(self, username=None, password=None, retry=True):
        self._username = username or self._username
        self._password = password or self._password
        if not isinstance(self._username, string_types) or not isinstance(self._password, string_types):
            raise InvalidCredentialsException("Username/password not correctly specified")

        self.log.info('PTC User Login for: {}'.format(self._username))
        self._session.cookies.clear()
        now = get_time()

        try:
            headers = {'Host': 'sso.pokemon.com',
                       'Connection': 'keep-alive',
                       'User-Agent': 'pokemongo/1 CFNetwork/811.4.18 Darwin/16.5.0',
                       'Accept-Language': self.locale.lower().replace('_', '-'),
                       'X-Unity-Version': '5.5.1f1',
                       'Content-Length': '-1'}
            r = self._session.get('https://sso.pokemon.com/sso/oauth2.0/authorize', timeout=self.timeout,
                                  headers=headers, params={'client_id': 'mobile-app_pokemon-go',
                                                           'redirect_uri': 'https://www.nianticlabs.com/pokemongo/error',
                                                           'locale': self.locale})
            data = r.json(encoding='utf-8', content_type=None)
            assert 'lt' in data and 'execution' in data

            data['_eventId'] = 'submit'
            data['username'] = self._username
            data['password'] = self._password
            data['locale'] = self.locale

            headers.update({
                'Content-Type': 'application/x-www-form-urlencoded'
            })

            # 2nd Request

            r = self._session.post(url='https://sso.pokemon.com/sso/login', headers=headers, params={'service': 'http://sso.pokemon.com/sso/oauth2.0/callbackAuthorize', 'locale': self.locale}, data=data)

            try:
                self._access_token = r.cookies['CASTGC'].value
            except (AttributeError, KeyError, TypeError) as e:
                raise AuthException(e)
        except Timeout:
            raise AuthTimeoutException('Auth timed out.')
        except RequestException as e:
            raise AuthException('Caught RequestException: {}'.format(e))

        if self._access_token:
            self._access_token_expiry = now + 7195.0
            self.log.info('PTC User Login successful.')

    def set_refresh_token(self, refresh_token):
        self.log.info('PTC Refresh Token provided by user')
        self._refresh_token = refresh_token

    def get_access_token(self, force_refresh=False):
        token_validity = self.check_access_token()

        if token_validity is True and force_refresh is False:
            self.log.debug('Using cached PTC Access Token')
            return self._access_token

        self._access_token = None
        self.user_login()
        return self._access_token