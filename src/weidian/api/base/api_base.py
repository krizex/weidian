#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from urllib import quote

import requests

from weidian.common.public import API_URL, TOKEN_ERR_CODE
from weidian.token.token_mgr import TokenManager

__author__ = 'David Qian'

"""
Created on 06/04/2016
@author: David Qian

"""


def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print '-----------START-----------'
    print('{}\n{}\n\n{}'.format(
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))
    print '-----------END-----------'


class ApiCallBase(object):
    _method = None
    _access_token = None
    _version = '1.0'
    _format = 'json'

    def __init__(self):
        self._access_token = TokenManager().get_token()

    def _update_token(self):
        TokenManager().update_token()
        self._access_token = TokenManager().get_token()

    def _get_public_params(self):
        d = {
            'method': self._method,
            'access_token': self._access_token,
            'version': self._version,
            'format': self._format,
        }

        return d

    def _invoke(self, business_params):
        req = self._build_request(business_params)
        rep = requests.Session().send(req)
        status_code = rep.json()['status']['status_code']
        if status_code not in TOKEN_ERR_CODE:
            return rep.json()

        # token error, refresh it and retry
        print 'token error, refresh it and retry'
        self._update_token()
        req = self._build_request(business_params)
        rep = requests.Session().send(req)
        return rep.json()

    def _build_request(self, business_params):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        payload = {
            'param': business_params,
            'public': self._get_public_params(),
        }

        params = []
        for k, v in payload.iteritems():
            params.append('%s=%s' % (k, quote(json.dumps(v))))

        req = requests.Request('POST', API_URL, headers=headers, data='&'.join(params))
        prepped_req = req.prepare()
        pretty_print_POST(prepped_req)
        return prepped_req

