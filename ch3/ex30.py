#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex30.py
@Time    :  2018/9/3 16:06
"""
'Else 和 IF'
people = 30
cars = 40
trucks = 15

if cars > people:
    print('We should take the cars.')
elif cars < people:
    print('We should not take the cars.')
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print('Maybe we could take the trucks.')
else:
    print('We still can\'t decide.')

if people > trucks:
    print('Alright, let\'s just take the trucks.')
else:
    print("Fine, let's stay home then.")
