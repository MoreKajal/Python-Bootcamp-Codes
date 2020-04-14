# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:53:47 2020

@author: Kajal
"""

# Range operator : Generator, it generates the function instead of saving to memory
for num in range(10):
    print(num)

# Using step size
for num in range(0, 11, 2):
    print(num)

# to get list in range of 10
list(range(0,10))

## enumerate

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

## OR
index_count = 0
word = 'abcde'
for letter in word:
    
    print(word[index_count])
    index_count += 1

## OR
word = 'abcde'
for item in enumerate(word):
    
    print(item)
## This give index count in the form of tuple
    
word = 'abcde'
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')
    
## Zip operator: zips all ogether to a list
# zip takes the pair of list items of size 
# equal to that of shortest length of list available
l1 = [1, 3, 5]
l2 = ['a', 'g', 3, 7]
for item in zip(l1, l2):
    print(item)
    
list(zip(l1, l2))

## in operator : to check that something is in list
'x' in [1,2,3]   # Returns false

'x' in ['a', 'x']  # Returns true

'a' in 'a world'    # True for string

'keys' in {'keys': 325}

d = {'keys': 325}
325 in d.values()
'keys' in d.keys()

# min and max operator
print(min(l1))
print(max(l1))

# random operator
from random import shuffle
list1 = [1,2,3,4,5,6,7,8,9]
shuffle(list1)
list1

from random import randint
randint(0, 100)
# This gives any random value between

## input operator : A;ways excepts a string
res = input('Enter something here')


