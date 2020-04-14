# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:13:06 2020

@author: Kajal
"""

## Instead of indexing use keys to access values.
prices = {'apple':200, 'mango': 250}
print('The value of apple is {}'.format(prices['apple']))

d = {'k1': 123, 'k2': [0, 1,2], 'k3':{'inside-key':100}}
print('value of k2 is', d['k2'])
print('value of k2 list of index 2 is', d['k2'][2])
print('value of k3 is', d['k3']['inside-key'])

d = {'key1':['a', 'b', 'c']}
print('the dictionary above is: ', d)
mylist = d['key1']
print('What is the list at value1 {}'.format(mylist))
# want to access letters from list and perform some operations
letter = mylist[2]
print('letter at index 2 :', letter.upper())

# Now instead of doing this can do like as:
print('letter at index 2 from dictionary:', d['key1'][2].upper())

# Add new key-value in existing dict
d['key2'] = 300
print('new dict is :', d)

#overwritting existing value
d['key2'] = 'New-value'
print('Overwrited dict is :', d)

