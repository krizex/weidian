#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

from weidian.common.public import TOKEN_URL
from weidian.utils.singleton import Singleton

__author__ = 'David Qian'

"""
Created on 06/04/2016
@author: David Qian

"""


APPKEY = '658401'
SECRET = '5779e979d8287c2a96dfec35640eb22c'


@Singleton
class TokenManager(object):
    def __init__(self):
        self._appkey = APPKEY
        self._secret = SECRET

    def get_token(self):
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
