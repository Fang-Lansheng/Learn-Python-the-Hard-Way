
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex39.py
@Time    :  2018/9/10 16:35
"""
'字典，可爱的字典'
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print('NY State has:', cities['NY'])
print('OR State has:', cities['OR'])

# print some states
print('-' * 10)
print('Michigan\'s abbreviation is:', states['Michigan'])
print('Florida\'s abbreviation is:', states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print('Michigan has:', cities[states['Michigan']])
print('Florida has:', cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, city in cities.items():
    print('%s has the city %s' % (state, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print('%s state is abbreviated %s and has city %s' %
          (state, abbrev, cities[abbrev]))

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')
# dict.get(key, default=None)：返回指定键的值，如果值不在字典中返回default的值
if not state:
    print('Sorry, no Texas.')

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: %s" % city)

