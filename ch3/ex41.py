#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex41.py
@Time    :  2018/9/19 16:28
"""
'学会说面向对象'

'单词解释'
'''
class（类）：告诉Python去创建一个新类型。
object（对象）：事物的基本类型，或事物的实例化
instance（实例）：通过Python创建一个类得到的
def：用来在类中定义一个函数
self：在一个类包含的函数中，self是一个用来访问实例或对象的变量
inheritance（继承）：表示一个类可以继承另一个类的特征
composition：表示一个类可以包含其他类
attribute：类所拥有的特性，通常是变量
is-a：惯用语，表示一个东西继承自另一个东西（a），如“鲑鱼”是“鱼”
has-a：惯用语，表示由其他事情或有一个特征（a），如“鲑鱼”有“嘴”
'''

'阅读测试'
import random   # 导入random模块
import urllib.request
import sys  # sys是Python自带模块

WORD_URL = 'http://learncodethehardway.org/words.txt'   # URL：统一资源定位符
WORDS = []  # WORD是一个用来存储word的list

PHRASES = {
    'class %%%(%%%):':
        'Make a class named %%% that is-a %%%.',
    'class %%%(object):\n\tdef __init__(self, ***)':
        'class %%% has-a __init__ that takes self and *** parameters.',
    'class %%%(object):\n\tdef ***(self, @@@)':
        'class %%% has-a function named *** that takes self and @@@ parameters.',
    '*** = %%%()':
        'Set *** to an instance of class %%%',
    '***.***(@@@)':
        'From *** get the *** function, and call it with parameters self, @@@',
    '***.*** = \'***\'':
        'From *** get the *** attribute and set it to \'***\'.'
}   # 短语集合

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

# load up the words from the website
# 从网站上加载单词，存储在WORD[]中
for word in urllib.request.urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())
    '''Python strip()方法用于移除字符串首位指定的字符（默认为空格）或字符序列'''

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count('%%%'))]
    '''
    class_names是类名
    Python capitalize()将字符串的第一个字母变成大写，其他字母变成小写
    random.sample()从WORDS(list)中随机获取num（=snippet中%%%出现次数）个单词
    '''
    other_names = random.sample(WORDS, snippet.count('***'))
    results = []
    param_names = []

    for i in range(0, snippet.count('@@@')):
        param_count = random.randint(1, 3)  # random.randint(1, 3)返回[1, 3]区间内数字（随机数）
        param_names.append(', '.join(random.sample(str(WORDS), param_count)))
        # param_names是变量名的list
        # random.sample()从WORDS中随机获取param_count个单词，这些单词以‘，’连接

    for sentence in snippet, phrase:
        result = sentence[:]    # 列表的分割切片语法[:]，得到列表从第一个到最后一个元素的切片

        # fake class names
        for word in class_names:
            result = result.replace('%%%', str(word), 1)
            # replace()，将字符串中的%%%用word替换，替换不超过1次

        # fake other names
        for word in other_names:
            result = result.replace('@@@', str(word), 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        # snippets = PHRASES.keys()
        snippets = list(PHRASES.keys())
        # dict.keys返回一个迭代器，可用list()来转换为列表，包含字典中的所有键
        random.shuffle(snippets)
        # random.shuffle()函数将序列中的所有元素随机排序

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question, answer = answer, question

            print(question)

            input('> ')
            print('ANSWER: %s\n\n' % answer)
except EOFError:
    print('\nBye')

















