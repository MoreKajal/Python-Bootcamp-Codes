# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:38:16 2020

@author: Kajal
"""

if True:
    print('Its TRUE !')
    
hungry = False
if hungry:
    print('Feed Me!')
else:
    print('No, Iam not hungry') 

loc = 'Bank'

if loc =='Auto shop':
    print(' Cars are cool! ' )    
elif loc == 'Bank':
    print('Money is cool!')
else:
    print('I do not know much')

## For loop
mylist = [1,2,3,4,5,6,7,8,9,10]
for i in mylist:
    print('whats here :', i)
    
for name in mylist:
    print('hello')

for num in mylist:
    if num % 2 == 0:
        print('Its even', num)
    else:
        print('odd number', num)

