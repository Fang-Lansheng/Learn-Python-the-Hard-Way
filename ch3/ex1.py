#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex1.py
@Time    :  2018/8/11 12:12
"""

print('Hello, world!')
print('Hello, Again')
print('I like typing this.')
print('This is fun.')
print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

print('I will now count my chickens:')
print('Hens', 25 + 30 / 6)
print('Roosters', 100 - 25 * 3 % 4)
print('Now I will count the eggs:')
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print(7.0 / 4.0, ',', 7 / 4)

print('-----------------------------------')
cars = 100  # 车辆数
space_in_car = 4.0  # 每辆车承载量
drivers = 30        # 驾驶员数量
passengers = 90     # 乘客数
cars_not_driven = cars - drivers    # 未被驾驶的车辆数
cars_driven = drivers       # 被驾驶的车辆数
carpool_capacity = cars_driven * space_in_car   # 车辆总承载量
average_passengers_per_car = passengers / cars_driven   # 平均每辆车承载量

print('There are', cars, 'cars available.')
print('There are only', drivers, 'drivers available.')
print('There will be', cars_not_driven, 'empty cars today.')
print('We can transport', carpool_capacity, 'people today.')
print('We have', passengers, 'to carpool today.')
print('We need to put about', average_passengers_per_car, 'in each car.')

print('====================================')
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74  # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d, then I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

print('-----------------------------------------')
x = "There are %d types of people." % 10
binary = 'binary'
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."
print(w + e)

print('------------------------------------------')
'更多的打印（输出）'
print("Mary had a little lamb.")
print("It's fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10)     # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happends
print(end1 + end2 + end3 + end4 + end5 + end6,
      end7 + end8 + end9 + end10 + end11 + end12)


print('-------------------------------')
'3.9 打印，打印'
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ('one', 'two', 'there', 'four'))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    'I had this thing.',
    'That you could type up right.',
    "But it didn't sing.",
    'So I said goodnight.'
))

print('---------------------------------')
'3.10 打印，打印，打印'
# Here's some new strange stuff, remember type it exactly.
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are days:", days)
print("Here are the months:", months)

print("""
    There's something going on here.
    With the three double-quotes.
    We'll be able to type as much as we like.
    Even 4 lines if we want, or 5, or 6.
""")

print('----------------------------------')
'3.11 那是什么？'
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# while True:
#     for i in ['/', '-', '|', '\\', '|']:
#         print('%s\r' % i)

print('--------------------------------------')
'提问'
# print("How old are you?")
# age = input()
# print('How tall are you?')
# height = input()
# print('How much do you weigh?')
# weight = input()
# print('So, you\'re %r old, %r tall and %r heavy.' % (age, height, weight))

print('---------------------------------------')
'提示别人'
# age = input('How old are you?\n')
# height = input('How tall are you?\n')
# weight = input('How much do you weigh?\n')
# print('So, you\'re %s years old, %scm tall and %skg heavy.' % (age, height, weight))

print('----------------------------------------')
'参数，解包，变量'
from sys import argv
# script, first, second, third = argv
#
# print('The script is called:', script)
# print('Your first variable is:', first)
# print('Your second variable is:', second)
# print('Your third variable is:', third)

print('-----------------------------------------')
'提示与传递'
from sys import argv

# script, user_name = argv
# prompt = '> '
#
# print('Hi %s, I\'m the %s script.' % (user_name, script))
# print('I\'d like to ask you a few questions.')
# print('Do you like me %s?' % user_name)
# likes = input(prompt)
#
# print('Where do you live %s?' % user_name)
# lives = input(prompt)
# print('What kind of computer do you have?')
# computer = input(prompt)
# print('''
# Alright, so you said %r about liking me.
# You live in %r. Not sure where that is.
# And you have a %r computer. Nice.
# ''' % (likes, lives, computer))
