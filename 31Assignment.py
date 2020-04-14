# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:14:10 2020

@author: Kajal
"""

## Problem1 : Handle the exception thrown by code below using try and except blocks
# Dont have typeerror pop up

for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError:
        print("Its showing TypeError")

## OR
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Its showing TypeError")
        
## Problem2 : Handle the exception thrown by code below using try and except blocks
# Then use finally block to print 'All Done'
    
x = 5
y = 0

z = x/y

## ANS:

try:
    x = 5
    y = 0
    z = x/y
except:
    print("There was a ZeroDivisionError")
finally:
    print("All Done")

## Problem 3 : Write a function for an integer and prints square of it. Use aa while loop with try, except, else block to account  for incorrect results
    
#def ask():
#    pass

## Ans:

def ask():
    while True:
        try:
            result = int(input("Please enter a number : " ))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("The square of the input number is:")
            print(result ** 2)
            break

ask()
