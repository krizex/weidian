#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import update_wrapper

__author__ = 'David Qian'

"""
Created on 06/04/2016
@author: David Qian

"""


class Singleton:
    """Singleton class decorator

    Use decorator to restricts the instantiation of a class to one object

    In Cafe, we use it is to declare a global object.

    Example:
        >>> @Singleton
        >>> class Foo(object): pass
        >>> f1 = Foo()
        >>> f2 = Foo()
        >>> f1 is f2
        True

    """

    def __init__(self, klass):
        self._klass = klass
        self._instance = None
        update_wrapper(self, klass)

    def __call__(self, *args, **kwds):

        if self._instance is None:
            self._instance = self._klass(*args, **kwds)

        return self._instance
