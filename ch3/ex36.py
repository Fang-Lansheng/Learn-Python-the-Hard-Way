#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex36.py
@Time    :  2018/9/10 11:52
"""
'设计与调试'

from sys import exit

def start():
    print('！~~~游-戏-开-始~~~！')
    print('饥肠辘辘的你来到了一家KFC前：')
    choice = input('进去饱餐一顿（输入1=是；输入2=否）> ')
    if choice == '1':
        scene1()
    elif choice == '2':
        print('你选择掉头就走。')
        print('有饭不吃，你饿晕在街头，被送到了医院。')
        game_over()
    else:
        shutdown()

def scene1():
    print('你进入了KFC')
    print('点好了餐，你发现只有两张桌子还有空位。')
    choice = input('你选择和谁坐（输入1=男生；输入2=女生）> ')
    if choice == '1':
        print('其实这个男生是你的男朋友，吃完饭你们要一起去逛街。')
        game_over()
    elif choice == '2':
        scene2()
    else:
        shutdown()


def scene2():
    print('你坐在了一个漂亮小姐姐的对面。正吃着饭，她的手机不小心掉到了你脚边。')
    choice = input('她看向你。是否要帮她捡起来（输入1=是；输入2=否）> ')
    if choice == '1':
        scene3()
    elif choice == '2':
        print('小姐姐看了你一眼，捡起手机气呼呼地走了。')
        game_over()
    else:
        shutdown()

def scene3():
    print('小姐姐非常感谢你，你们愉快地聊了很久，临走前，她问你可以留下联系方式吗？')
    print('你发现她对你有意思，但你知道自己是个gay。所以你选择：')
    choice = input('（输入1=同意；输入2=拒绝）> ')
    if choice == '1':
        print('“好啊，我的电话是13XXXXXXXXX”')
        game_over()
    elif choice == '2':
        print('guna!老子最讨厌女人了！')
        game_over()
    else:
        shutdown()

def game_over():
    print('|***游-戏-结-束***|')
    exit(0)

def shutdown():
    print('输入错误，游戏终止！')
    BaseException()

start()
