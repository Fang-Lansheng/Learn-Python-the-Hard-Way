#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex44.py
@Time    :  2018/9/20 16:18
"""
'继承 VS. 包含'

'什么是继承' \
'> 继承是用来描述一个类从它的父类那里获得大部分甚至全部父类的功能' \
'父子类之间有3中交互方法' \
'> 1. 子类的方法隐性继承父类方法' \
'> 2. 子类重写父类的方法' \
'> 3. 对子类的操作改变父类'

print('-' * 10)
'隐性继承'
class Parent(object):
    def implict(self):
        print('PARENT implict()')

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implict()
son.implict()

print('-' * 10)
'重写方法'
class Parent(object):
    def override(self):
        print('PARENT override()')

class Child(Parent):
    def override(self):
        print('CHILD override()')

dad = Parent()
son = Child()

dad.override()
son.override()

print('-' * 10)
'之前或之后改变父类'

class Parent(object):
    def altered(self):
        print('PARENT altered()')

class Child(Parent):
    def altered(self):
        print('CHILD, BEFORE PARENT altered()')
        # super()函数是用于调用父类（超类）的一个方法
        # super(Child, self).altered()
        super().altered()   # Python 3中可以直接使用该用法
        print('CHILD, AFTER PARENT altered()')

dad = Parent()
son = Child()

dad.altered()
son.altered()

print('-' * 10)
'三种组合使用'

class Parent(object):
    def override(self):
        print('PARENT override()')

    def implicit(self):
        print('PARENT implicit()')

    def altered(self):
        print('PARENT altered()')

class Child(Parent):
    def override(self):
        print('CHILD override()')

    def altered(self):
        print('CHILD, BEFORE PARENT override()')
        super().altered()
        print('CHILD, AFTER PARENT override()')

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

print('-' * 10)
'使用super()的原因'

class BadStuff(object):
    pass

class SuperFun(Child, BadStuff):
    pass


print('-' * 10)
'包含'

class Other(object):
    def override(self):
        print('OTHER override()')

    def implicit(self):
        print('OTHER implicit()')

    def altered(self):
        print('OTHER altered()')

class Child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print('CHILD override()')

    def altered(self):
        print('CHILD, BEFORE OTHER altered()')
        self.other.altered()
        print('CHILD, AFTER OTHER altered()')

son = Child()

son.implicit()
son.override()
son.altered()
