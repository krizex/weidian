#!/usr/bin/env python
# -*- coding: utf-8 -*-
from weidian.token.token_mgr import TokenManager

__author__ = 'David Qian'

"""
Created on 06/04/2016
@author: David Qian

"""


class Payment(object):
    def __init__(self):
        self._token = TokenManager().get_token()[0]

    def get_qr_code(self):
        pass