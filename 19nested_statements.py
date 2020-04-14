# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:09:35 2020

@author: Kajal
"""

x = 25

def printer():
    x = 50
    return x
print(x)      # output = 25

print(printer())  # output = 50

# 1. Local
lambda num : num ** 2  # num is local to lambda

# 2. Enclosing local function
# first create a function and then put a function inside it
# Local name space is within a function

name = 'This is a global string'     # name :defined as global

def greet():
#    name = 'Sammy'        # name defines as local enclosing function
    def hello():
        print('Hello', name)
    hello()
greet()         # >> Hello Sammy

# Now if you comment out 'Sammy' it will take global name
# out >> Hello This is a global string


#####
# Global name
name = 'This is a global string'     # name :defined as global
def greet():
    # Enclosing
    name = 'Sammy'        # name defines as local enclosing function
    def hello():
        # Local
        name = 'I am local'
        print('Hello', name)
    hello()
greet()      # out>>  Hello I am local

## Above all there is : built in function
help(len)


## Example : if you want to use a global variable initially and then reassign some new value to it
x = 50
def func(x):
    print(f'x is {x}')
    #Local reassignment
    x = 'New Value'
    print(f' I just locaaly changed Global x to local {x}')
    return x
print(x)

x = func(x)
