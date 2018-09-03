#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex23.py
@Time    :  2018/8/20 15:16
"""
'阅读代码' \
'以下代码来自github.com' \

'例1 key_gen.py'
# https://github.com/Show-Me-the-Code/python/blob/master/AK-wang/0001/key_gen.py
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？

# import string   # 作用：包含处理文本的常量和类
# import random   # 作用：生成随机数
#
# KEY_LEN = 20
# KEY_ALL = 200
#
#
# def base_str():
#     return (string.ascii_letters + string.digits)   # 生成所有的字母和数字
# # >>> chars = string.ascii_letters + string.digits
# # >>> print(chars)
# # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
#
# def key_gen():
#     '''
#     生成激活码
#     :return: 激活码
#     '''
#     keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
#     # random.choice()方法返回一个列表、元组或字符串的随机项
#     return ("".join(keylist))
#     # str.join(sequence)方法用于将序列中的元素以指定的字符连接生成一个新的字符串
#     # 在此处，生成一个由随机数字和大小写字母组成的长度为20的字符串
#
# def key_num(num, result=None):
#     '''
#     将num个激活码组成一个list
#     :param num: 激活码数目
#     :param result: 将要输出的list
#     :return:
#     '''
#     if result is None:
#         result = [] # result为一个list
#     for i in range(num):
#         result.append(key_gen())
#     return result   # 返回一个包含了num个字符串（激活码）的list
#
#
# def print_key(num):
#     '''
#     打印激活码
#     :param num: 激活码数目
#     :return:
#     '''
#     for i in key_num(num):
#         print(i)    # 打印出字符串的每一个元素（字符/激活码）
#
#
# if __name__ == "__main__":
# # 当.py文件被直接运行时，其下的代码块将被运行。当.py以模块形式被导入时，其下的代码块不会被运行
#     print_key(KEY_ALL)  # 打印出KEY_ALL个激活码

'例2 key_gen_deco.py'
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？

import string   # 作用：包含处理文本的常量和类
import random   # 作用：生成随机数

KEY_LEN = 20    # 激活码长度为20
KEY_ALL = 200   # 激活码数目为200

def base_str():
    return (string.ascii_letters + string.digits)   # 生成所有的字母和数字
# >>> chars = string.ascii_letters + string.digits
# >>> print(chars)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

def key_gen():
    '''
    生成激活码
    :return: 激活码
    '''
    keyList = [random.choice(base_str()) for i in range(KEY_LEN)]
    # random.choice()方法返回一个列表、元组或字符串的随机项
    return (''.join(keyList))
    # str.join(sequence)方法用于将序列中的元素以指定的字符连接生成一个新的字符串
    # 在此处，生成一个由随机数字和大小写字母组成的长度为KEY_LEN=20的字符串

def print_key(func):    # print_key是一个装饰器，接受一个函数作为参数，并返回一个函数
    '''
    打印激活码
    :param func:
    :return:
    '''
    def _print_key(num):
        for i in func(num):
            print(i)
    return _print_key

@print_key  # 调用key_num()函数时，不仅会运行key_num()函数本身，也会运行print_key()函数
def key_num(num, result=None):
    '''
    :param num: 激活码数目
    :param result:
    :return: 一个list
    '''
    if result is None:
        result = []     # result为一个list
    for i in range(num):
        result.append(key_gen())    # 向这个list中添加一个key（激活码）
    return result   # 返回包含了num个key（激活码）的list

if __name__ == '__main__':
    # 当.py文件被直接运行时，其下的代码块将被运行。当.py以模块形式被导入时，其下的代码块不会被运行
    # print_key(KEY_ALL)
    key_num(KEY_ALL)

