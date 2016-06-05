#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os

import requests
import time

from weidian.common.public import TOKEN_URL
from weidian.token.my_token import MY_APPKEY, MY_SECRET
from weidian.utils.singleton import Singleton

__author__ = 'David Qian'

"""
Created on 06/04/2016
@author: David Qian

"""


APPKEY = MY_APPKEY
SECRET = MY_SECRET


@Singleton
class TokenManager(object):
    _PERSISTENT_FILE = os.path.join(os.path.dirname(__file__), 'token_file')

    def __init__(self):
        self._appkey = APPKEY
        self._secret = SECRET
        self._token, self._expire_in = self._recover_token()

    def get_token(self):
        # TODO: check whether token is expired
        return self._token

    def update_token(self):
        self._token, self._expire_in = self._get_token()
        self._save_token()
        return self._token, self._expire_in

    def _save_token(self):
        save_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        js_data = {
            'save_time': save_time,
            'access_token': self._token,
            'expire_in': self._expire_in,
        }

        with open(self._PERSISTENT_FILE, 'w') as f:
            json.dump(js_data, f)

    def _recover_token(self):
        if not os.path.isfile(self._PERSISTENT_FILE):
            return self.update_token()

        with open(self._PERSISTENT_FILE) as f:
            js_data = json.load(f)

        access_token = js_data['access_token']
        expire_in = js_data['expire_in']
        save_time = js_data['save_time']
        save_time = time.mktime(time.strptime(save_time, '%Y-%m-%d %H:%M:%S'))
        expire_in = expire_in - (time.time() - save_time)
        if expire_in <= 0:
            access_token, expire_in = self._update_token()

        return access_token, expire_in

    def _get_token(self):
        print '_get_token'
        payload = {
            'grant_type': 'client_credential',
            'appkey': self._appkey,
            'secret': self._secret,
        }
        r = requests.get(TOKEN_URL, params=payload)
        result = r.json()
        print result
        if result['status']['status_code'] == 0:
            return result['result']['access_token'], result['result']['expire_in']
        else:
            return None, None

if __name__ == '__main__':
    tm = TokenManager()
    tm.get_token()
