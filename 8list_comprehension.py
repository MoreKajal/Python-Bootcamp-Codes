# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:26:43 2020

@author: Kajal
"""


## List comprehension :
mystring = 'Hello'
mylist = []

for letter in mystring:
    mylist.append(letter)
mylist

# OR
mylist = []
letter = [letter for letter in mystring]
mylist

mylist = [x for x in range(0,11)]
mylist

# To get square of elements in list
mylist = [x**2 for x in range(0,11)]
mylist

# Taking only even elements
mylist = [x**2 for x in range(0,11) if x % 2 == 0]
mylist

# if else inside list comprehension
res = [x if x %2 ==0 else 'odd' for x in range(0,11)]
res

# nested loop
list = []
for x in [2,4,6]:
    for y in [100,200,300]:
        list.append(x*y)
list

# Can be done as
mylist = [x*y for x in [2,4,6] for y in [100, 200, 300]]
mylist