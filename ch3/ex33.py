#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex33.py
@Time    :  2018/9/9 19:22
"""
'while循环'

i = 0
numbers = []

while i < 6:
    print('At the top i is %d' % i)
    numbers.append(i)

    i = i + 1
    print('Numbers now:', numbers)
    print('At the button i is %d' % i)

print('The numbers:')
for num in numbers:
    print(num)
