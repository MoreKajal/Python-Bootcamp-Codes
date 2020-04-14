# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:48:15 2020

@author: Kajal
"""

## namedtuple

t = (1,2,3)
t[0]    # >>1

from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')
## Note here : wee can pass multiple arhuments in single string
sam = Dog(age = 2, breed = 'Lab', name = 'Samy')

sam.age

sam[2]

