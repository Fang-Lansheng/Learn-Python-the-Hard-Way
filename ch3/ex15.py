#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex15.py
@Time    :  2018/8/12 10:56
"""

print('读文件')
from sys import argv
script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input('> ')
txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
