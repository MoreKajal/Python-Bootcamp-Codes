# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:46:55 2020

@author: Kajal
"""

# Assessment test 1
## Q4 : Get 'hello' from given

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print('Getting hello from above : ', d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky', {'tough':[1,2,['hello']]}]}]}
print('Getting hello from above :', d['k1'][2]['k2'][1]['tough'][2][0])

## Q5 : Use set to find unique values of list below
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print('Get set from list5 :', set(list5))

## Q6 : What is boolean output for below
l1 = [1,2,[3,4]]
l2 = [1,2, {'k1':4}]

l1[2][0] >= l2[2]['k1']