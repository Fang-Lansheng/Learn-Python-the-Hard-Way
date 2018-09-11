#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  hashmap.py
@Time    :  2018/9/11 21:31
"""


def new(num_buckets=256):
    '''Initializes a Map with the given number of buckets'''
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

def hash_key(aMap, key):
    '''Given a key this will create a number and
    then convert it to an index for the aMap\'s buckets'''
    return hash(key) % len(aMap)
# hash()用于获取一个对象（字符串或者数值等）的哈希值
