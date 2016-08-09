#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""accept-tos.py: Example script to accept in-game Terms of Service"""
import time

from pgoapi import PGoApi


def accept_tos(username, password, auth='ptc'):
    api = PGoApi()
    api.set_position(40.7127837, -74.005941, 0.0)
    api.login(auth, username, password)
    time.sleep(2)
    req = api.create_request()
    req.mark_tutorial_complete(tutorials_completed=0, send_marketing_emails=False, send_push_notifications=False)
    response = req.call()
    print('Accepted Terms of Service for {}'.format(username))
    # print('Response dictionary: \r\n{}'.format(pprint.PrettyPrinter(indent=4).pformat(response)))

"""auth service defaults to ptc if not given"""

accept_tos('username', 'password')
accept_tos('username2', 'password', 'ptc')
accept_tos('username3', 'password', 'google')
