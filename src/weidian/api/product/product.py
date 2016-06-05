#!/usr/bin/env python
# -*- coding: utf-8 -*-
from weidian.api.base.api_base import ApiCallBase

__author__ = 'David Qian'

"""
Created on 06/05/2016
@author: David Qian

"""


class Product(ApiCallBase):
    _method = 'vdian.item.list.get'

    def __init__(self):
        super(Product, self).__init__()

    def get_all_products(self):
        business_params = {
            'page_num': 1,
            'orderby': 1,
            'page_size': 30,
        }

        r = self._invoke(business_params)
        print r

if __name__ == '__main__':
    p = Product()
    p.get_all_products()