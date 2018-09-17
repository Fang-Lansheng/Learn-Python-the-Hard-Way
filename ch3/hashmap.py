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

'hashmap：拥有键值对的有插槽的列表' \
'aMap：一个列表变量' \



def new(num_buckets=256):   # 即hashmap.new()
    '''Initializes a Map with the given number of buckets'''
    '''用给定数目的bucket（存储空间）初始化一个Map（映射）。'''
    # 以下为官方文档中给出的解释
    '> 首先，创建一个函数来生成一个hashmap（初始化）' \
    '> 先创建一个包含列表的变量，叫做aMap，然后把num_buckets（用以存放给hashmap设置的内容）放进去'
    aMap = []   # aMap是一个list
    for i in range(0, num_buckets):
        aMap.append([]) # 列表aMap的每一个元素都是一个列表
    return aMap

def hash_key(aMap, key):    # 即hashmap.hash_key(key)
    '''Given a key this will create a number and
    then convert it to an index for the aMap\'s buckets.'''
    '给定一个键值，hash_key()会返回一个可以用作索引的哈希值'
    '> hash_key是一个dict如何工作的核心。' \
    '> 用Python内建的哈希函数（hash）将字符串（key）转换为数字' \
    '> hash(key)即为key对应的数字，使用模除（%）操作和len(aMap)来获得一个放置这个key的位置' \
    '> 模除（%）操作将会返回除法操作的余数，可以用来限制大数，将其转换为较小的一组数字'
    return hash(key) % len(aMap) # 利用模除（%）操作，将这个哈希值转换为bucket的索引
# hash()用于获取一个对象（字符串或者数值等）的哈希值

def get_bucket(aMap, key):  # 即hashmap.get_bucket(key)
    '''Given a key, find the bucket where it would go.'''
    '给定一个键值，将作为其索引的哈希值存储在映射list:aMap中'
    '> get_bucket函数使用hash_key来找到一个key所在的“bucket”' \
    '> 无论获得哪一个bucket_id都会填充进aMap列表中，使用bucket_id可以找打一个key所在的“bucket”'
    bucket_id = hash_key(aMap, key) # bucket_id是一个哈希值，作为键值对的索引
    return aMap[bucket_id]

def get_slot(aMap, key, default=None):
    '''
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key, and default (None if not set) when not found.
    '''
    '> get_slot函数使用get_bucket来获得一个key所在的“bucket”' \
    '> 通过查找bucket中的每一个元素来找到对应的key。找到对应的key之后，它会返回一个这样的元组(i,k,v)' \
    '> i表示的是key的索引值，k就是key本身，v就是key对应的值'
    bucket = get_bucket(aMap, key)
    for i, kv in enumerate(bucket):
    # enumerate()函数用于将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标，一般用在for循环中
    # i：index（索引）; kv：bucket中的元素，由key（键值，k）和value（键对应的值，v）（bucket是一个列表，也是aMap中的一个元素）
        k, v = kv
        if key == k:
            return i, k, v  # 返回index（索引），key（键），value（值）

    return -1, key, default

'类似于dict.get(key, default=None)，返回指定键的值，如果值不存在则返回default值'
def get(aMap, key, default=None):
    '''Gets the value in a bucket for the given key, or the default.'''
    '> get这是一个人们需要hashmap的最方便的函数。' \
    '> 它使用get_slot来获得元组(i,k,v)，但只是返回v。'
    i, k, v = get_slot(aMap, key, default=default)
    return v

def set(aMap, key, value):  # 即hashmap.set(key, value)
    '''Sets the key to the value, replacing any existing value.'''
    "给字典aMap赋予一组键值key=>value"
    '> set设置一个key/value 键/值对，并将其追加到字典中，保证以后再用到时可以获取得到' \
    '> 为保证hashmap中的每个key只存储一次：首先要找到这个key是否已经存在' \
    '> 如果存在，会替换其原来的值；如果不存在，则会追加进来'
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)   # i，k，v分别是index，key和value

    if i >= 0:
        # the key exists, replace it
        # 如果key存在，替换之
        bucket[i] = (key, value)
    else:
        # the key does not, append to create it
        # 如果键key不存在，则增加
        bucket.append((key, value))

'删除字典中指定键的值'
def delete(aMap, key):
    '''Deletes the given key from the Map.'''
    '> delete 删除一个key：找到key对应的bucket，并将其从列表中删除' \

    bucket = get_bucket(aMap, key)

    for i in range(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]   # 使用del语句来删除列表中的元素（删除列表bucket中索引为i的元素）
            break   # 用于终止循环语句，用在while和for循环中

'打印出字典中的元素'
def list(aMap):
    '''Prints out what\'s in the Map.'''
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                # print(k, v)
                print('\'', k, '\':', v)

