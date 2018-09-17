#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  hashmap.py
@Time    :  2018/9/11 21:31
"""
'定义自己的字典类'
'''
用list来创建一个字典数据结构hashmap
'''

def new(num_buckets=256):   # 即hashmap.new()
    '''Initializes a Map with the given number of buckets'''
    '''用给定数目的bucket（存储空间）初始化一个Map（映射）。'''
    aMap = []   # aMap是一个list
    for i in range(0, num_buckets):
        aMap.append([]) # 列表aMap的每一个元素都是一个列表
    return aMap

def hash_key(aMap, key):    # 即hashmap.hash_key(key)
    '''Given a key this will create a number and
    then convert it to an index for the aMap\'s buckets.'''
    '给定一个键值，hash_key()会返回一个可以用作索引的哈希值'
    return hash(key) % len(aMap) # 哈希值长度为aMap列表长度
# hash()用于获取一个对象（字符串或者数值等）的哈希值

def get_bucket(aMap, key):  # 即hashmap.get_bucket(key)
    '''Given a key, find the bucket where it would go.'''
    '给定一个键值，将作为其索引的哈希值存储在映射list:aMap中'
    bucket_id = hash_key(aMap, key) # bucket_id是一个哈希值，作为键值对的索引
    return aMap[bucket_id]

def get_slot(aMap, key, default=None):  # 即hashmap.get_slot(key, default=None)
    '''
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key, and default (None if not set) when not found.
    '''
    bucket = get_bucket(aMap, key)
    for i, kv in enumerate(bucket):
    # enumerate()函数用于将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标，一般用在for循环中
    # i：index（索引）; kv：bucket中的元素，由key（键值，k）和value（键对应的值，v）（bucket是一个列表，也是aMap中的一个元素）
        k, v = kv
        if key == k:
            return i, k, v  # 返回index（索引），key（键），value（值）

    return -1, key, default

'同dict.get(key, default=None)，返回指定键的值，如果值不再字典中返回default值'
def get(aMap, key, default=None):
    '''Gets the value in a bucket for the given key, or the default.'''
    i, k, v = get_slot(aMap, key, default=default)
    return v

def set(aMap, key, value):  # 即hashmap.set(key, value)
    '''Sets the key to the value, replacing any existing value.'''
    "给字典aMap赋予一组键值key=>value"
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)

    if i >= 0:
        # the key exists, replace it
        bucket[i] = (key, value)
    else:
        # the key does not, append to create it
        bucket.append((key, value))

'删除字典中指定键的值'
def delete(aMap, key):
    '''Deletes the given key from the Map.'''
    bucket = get_bucket(aMap, key)

    for i in range(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break

'打印出字典中的元素'
def list(aMap):
    '''Prints out what\'s in the Map.'''
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print(k, v)

