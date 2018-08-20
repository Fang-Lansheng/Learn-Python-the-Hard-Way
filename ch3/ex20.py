#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex20.py
@Time    :  2018/8/20 14:51
"""

'函数与文件'

from sys import argv
script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):  # 倒带（重新读取）
    f.seek(0)   # 重新设置文件读取指针到开头

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
