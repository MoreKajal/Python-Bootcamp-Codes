# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:34:19 2020

@author: Kajal
"""

## While loops

x = 0 
while x<5:
    print(f'The current value of x is {x}')
# This loop iterates over and over for n iterations
    
while x<5:
    print(f'The current value of x is {x}')
    x = x+1
#This loop iterates for 5 times from 0 to 4
    
x = 0
while x<5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print('x is not less than 5')  

## Break, continue, pass

x = [1,2,3]
for item in x:
    # Comment
    pass
print('Here if pass is not given and nothing is written in comment section it trows error')

mystring = "Hello"
for letter in mystring:
    if letter == 'e':
        continue
    print(letter)
# Here above if the letter is 'e' go back to the loop and continue iterating

mystring = "Hello"
for letter in mystring:
    if letter == 'e':
        break
    print(letter)
# Here it breaks out of the loop
    
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1

