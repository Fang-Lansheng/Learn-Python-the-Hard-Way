#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex29.py
@Time    :  2018/9/3 16:02
"""
'IF语句'

people = 20
cats = 30
dogs = 15

if people < cats:
    print('Too many cats! The world is doomed!')

if people > cats:
    print('Not many cats! The world is saved!')

if people < dogs:
    print('The world is drooled on!')

if people > dogs:
    print('The world is dry!')

dogs += 5

if people >= dogs:
    print('People are greater than or equal to dogs.')

if people <= dogs:
    print('People are less than or equal to dogs.')

if people == dogs:
    print('People are dogs.')
