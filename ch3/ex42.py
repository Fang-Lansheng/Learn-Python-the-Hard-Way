#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex42.py
@Time    :  2018/9/19 19:56
"""
'对象、类以及从属关系'

##  Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ??
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        # super(Employee, self).__init__(name)
        super().__init__(name)
        # 在Python 3中可以改为super().__init__(name)
        '''
        super()函数是用于调用父类（超类，此处为Person）的一个方法，是用来解决多重继承问题的
        直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到种种问题
        '''
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish): # salmon:鲑鱼
    pass

## ??
class Halibut(Fish):    # halibut：大比目鱼
    pass

## rover is-a dog
rover = Dog('Rover')

## satan is-a cat
satan = Cat('Satan')

## mary is-a person
mary = Person('Mary')

## frank is-a employee and his salary is 120000
frank = Employee('Frank', 120000)

## frank has-a pet and it's rover
frank.pet = rover

##
flipper = Fish()

## ??
crouse = Salmon()   # crouse:活泼的，大胆的

## ??
harry = Halibut()
