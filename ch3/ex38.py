#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex38.py
@Time    :  2018/9/10 15:09
"""
'列表操作'

ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print('Wait there are not 10 things in that list. Let\' fix that.')

stuff = ten_things.split(' ')   # split()通过指定分隔符对字符串进行切片
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
    next_one = more_stuff.pop() # pop()函数用于移除列表中的一个元素（默认是最后一个元素），并且返回该元素的值
    print("Adding: ", next_one)
    stuff.append(next_one)  # append()方法用于在列表末尾添加新的对象
    print('There are %d items now.' % len(stuff))

print('There we go:', stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))  # join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串
print('#'.join(stuff[3:5]))
