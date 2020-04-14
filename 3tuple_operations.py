# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:50:38 2020

@author: Kajal
"""

t = (1,2,3)
print('length of tuple: ', len(t))

t = ('one', 2)
print('At 1st index : ', t[0])

# Count and Indexing
t = ('a', 'a', 'b')
print('Count of a is {}'.format(t.count('a')))
# Indexing only gives starting position 
print('Index of a is {}'.format(t.index('a')))

## as in list we can reassign items but in tuple once 
## item is assigned we cannot replace it, it throws error


