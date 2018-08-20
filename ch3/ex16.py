#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex16.py
@Time    :  2018/8/12 11:04
"""

print('读写文件')
from sys import argv
script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input('?')

print('Opening the file...')
target = open(filename, 'w')
print('Truncating the file. Goodbye!')
target.truncate()
# truncate()方法用于从文件的首行首字符开始截断，无[size]表示从当前位置截断
# 截断之后后面的所有字符被删除

print("Now I'm going to ask you for three lines.")

line1 = input('line 1: ')
line2 = input('line 2: ')
line3 = input('line 3: ')

print("I'm going to write these to the file.")
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('And finally, we close it.')
target.close()
