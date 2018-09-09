#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex32.py
@Time    :  2018/9/6 19:46
"""
'循环和列表'

'list'
hairs = ['brown', 'blood', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print('This is count %d' % number)

# same as above
for fruit in fruits:
    print('A fruit of type: %s' % fruit)

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print('I got %r' % i)

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    '''
    range(start, stop[, step])
    - start: 计数从start开始。默认是从0开始。例如range(5)等价于range(0, 5)
    - stop:  计数到stop结束，但不包括stop。例如：range(0, 5)是[0, 1, 2, 3, 4]，没有5
    - step:  步长，默认为1。例如：range(0, 5)等价于range(0, 5, 1)
    '''
    print('Adding %d to the list.' % i)
    # append is a function that lists understand
    elements.append(i)

# now we can print them out
for i in elements:
    print('Element was: %d' % i)

