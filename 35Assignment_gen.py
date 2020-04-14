# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:00:34 2020

@author: Kajal
"""

## Q1 : create a generator that generates squares of numbers upto some number n

def gen_squares(n):
    for x in range(n):
        yield x**2

for number in gen_squares(10):
    print(number)


## Q2 : Create a generator that yields'n' random numbers between low and high numbers(that are input)

import random
random.randint(1, 10)

def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)
        
for num in rand_num(1,10, 12):
    print(num)

## Q3 : Use iter function to convert the string into an iterator
s = 'hello'

s_iter = iter(s)

print(next(s_iter))

## Q4: What a gencomp below
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

# >> 4    5
    