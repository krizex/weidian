#!/usr/bin/env python
# -*- coding: utf-8 -*-
from weidian.api.base.api_base import ApiCallBase

__author__ = 'David Qian'

"""
Created on 06/04/2016
@author: David Qian

"""


class Payment(ApiCallBase):
    _method = 'vdian.f2f.qrcode.get'

    def __init__(self):
        super(Payment, self).__init__()

    def get_qr_code(self):
        business_params = {

        }

        r = self._invoke(business_params)
        print r


if __name__ == '__main__':
    payment = Payment()
    payment.get_qr_code()
