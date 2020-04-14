# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:22:25 2020

@author: Kajal
"""

my_list = ['String', 100, 20.3]
l = len(my_list)
print('The length of list is {}'.format(l))

list2 = ['one', 'to']
print('List concatenated are {}'.format(my_list + list2))

list_n = my_list + list2
list_n.append('new')
print('List appended are {}'.format(list_n))
print('List pop item is : {}'.format(list_n.pop()))
print('List pop item from index position is : {}'.format(list_n.pop(2)))
new_list = ['a', 'g', 'k', 'b', 'r']
new_list.sort()       # As the sorted returns none at this, so print on next line
print('List of sorted item is : {}'.format(new_list))
new_list.reverse()
print('List of reversed item is : {}'.format(new_list))


