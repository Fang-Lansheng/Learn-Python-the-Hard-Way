#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex40.py
@Time    :  2018/9/17 20:33
"""
'模块，类和对象'

'模块就像字典'
# 可以认为一个模块就是一个可以存放Python代码的特殊字典，并且可以通过“.”操作符来访问它
mystuff = {'apple': 'I AM APPLES!'}
print(mystuff['apple']) # get apple from dict

# mystuff.py
import mystuff
mystuff.apple() # get apple from the module
print(mystuff.tangerine)    # same thing, it's just a variable


print('-' * 10)
'类就像模块'
# 类的作用是组织一系列的函数和数据并将它们放在一个容器里，这样也可以通过"."操作符来访问
class MyStuff(object):
    def __init__(self):
    # __init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    # self代表类的实例，self再定义类的方法时时必需的，虽然在调用时不必传入相应的参数
        self.tangerine = 'And now a thousand years between'
    def apple(self):
        print('I AM CLASSY APPLES!')

'对象就像导入'
thing = MyStuff()   # 实例化类的方法就是像调用函数一样调用这个类
'> Python查找MyStuff()并确认它是你已经定义过的类' \
'> Python创建一个空的对象，该对象拥有你在类中用def创建的所有函数' \
'> Python看你是否创建了__init__函数，如果有，调用该方法初始化你新创建的空对象' \
'> 在MyStuff中，__init__方法有一个额外的变量self，这是Python为我创建的一个空的对象，我可以在其上设置变量' \
'> 然后，我给self.tangerine设置一首歌词（一个字符串），然后初始化这个对象' \
'> Python可以使用这个新创建好的对象，并将其分配给我可以使用的变量thing'
thing.apple()
print(thing.tangerine)

'''
1. 类时用来创建迷你模块的蓝本或定义
2. 实例化是如何创建这些小模块，并在同一时间将其导入。实例化仅仅是指通过类创建一个对象。
3. 由此产生的迷你模块被称为对象，你可以将其分配给一个变量，让它开始运行。
'''

print('-' * 10)
'类的举例'
class Song(object): # object为所有类的基类
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(['Happy birthday to you',
                   'I don\'t want to get sued',
                   'So I\'ll stop right there'])

bulls_on_parade = Song(['They rally around tha family',
                        'With pockets full of shells'])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
