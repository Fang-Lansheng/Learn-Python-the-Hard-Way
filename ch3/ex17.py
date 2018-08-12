#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex17.py
@Time    :  2018/8/12 11:17
"""

'更多文件操作' \
'现在让我们再学习几种文件操作。' \
'我们将编写一个Python脚本，将一个文件中的内容拷贝到另外一个文件中。' \
'这个脚本很短，不过它会让你对于文件操作有更多的了解。'

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Coping from %s to %s" % (from_file, to_file))

# We could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()
indata = open(from_file).read()

print("The input file is %d bytes long." % len(indata))

print('Does the output file exists? %r' % exists(to_file))
print('Ready, hit RETURN to continue, CTRL-C to abort.')
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print('Alright, all done!')
out_file.close()
