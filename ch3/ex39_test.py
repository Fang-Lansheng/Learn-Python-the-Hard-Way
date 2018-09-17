#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex39_test.py
@Time    :  2018/9/11 21:24
"""
'定义自己的字典类'
import hashmap

# create a mapping of state to abbreviation
# 创建字典{state}，默认长度为256
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')     # 向字典中添加新的键/值对
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
# 创建字典{cities}，默认长度为256
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')  # 向字典中添加新的键/值对
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

# add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# print out some cities
# 打印出一些城市（打印出一些{cities}字典中的值）
print('-' * 10)
print('NY State has: %s' % hashmap.get(cities, 'NY'))
print('OR State has: %s' % hashmap.get(cities, 'OR'))

# print some states
print('-' * 10)
print('Michigan\'s abbreviation is: %s' % hashmap.get(states, 'Michigan'))
print('Florida\'s abbreviation is: %s' % hashmap.get(states, 'Florida'))

# do it by using the state then cities dict
print('-' * 10)
print('Michigan has: %s' % hashmap.get(cities, hashmap.get(states, 'Michigan')))
print('Florida has: %s' % hashmap.get(cities, hashmap.get(states, 'Florida')))

# print every state abbreviation
print('-' * 10)
hashmap.list(states)

# print every city in state
print('-' * 10)
hashmap.list(cities)

print('-' * 10)
state = hashmap.get(states, 'Texas')
if not state:
    print('Sorry, no Texas.')

# default values using ||= with nil result
# can you do this on the line?
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print('The city for the state \'TX\' is: %s' % city)
