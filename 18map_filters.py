# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:52:00 2020

@author: Kajal
"""

def square(num):
    return num ** 2

my_nums = [1,2,3,4,5]
map (square, my_nums)  ## this gives some memory location

# to print result, iterate through it
for item in map(square, my_nums):
    print(item)

# Generating a list from it    
list(map(square, my_nums))

# map for string

def splicer(mystring):
    if len(mystring) % 2 ==0:
        return 'Even'
    else:
        return mystring[0]
names = ['Andy', 'Eve', 'Sally']
list(map(splicer, names))    # ['Even', 'E', 'S']  --->Even for even letters in a name, rest with first letter


## Fiter function
def check_even(num):
    return num%2 ==0

my_nums = [1,2,3,4,5,6]

filter(check_even, my_nums)

list(filter(check_even, my_nums))

for n in filter(check_even, my_nums):
    print(n)
    
## Lambda expressions

def square(num):
    result = num ** 2
    return result

# Now, step by step convert into an expression
    
def square(num):
    return  num ** 2
# OR 
def square(num): return  num ** 2

# Next
square = lambda num: num ** 2 # this is lambda expression

square(5)

# OR
list(map(lambda num : num ** 2, my_nums))   # --> [1, 4, 9, 16, 25, 36]

## Check filters for lambda expressions
#lambda num:  num%2 ==0
#filter(lambda num:  num%2 ==0, my_nums)
list(filter(lambda num:  num%2 ==0, my_nums))

## Eg : Lambda expression to grab first character from string

names = ['Andy', 'Eve', 'Sally']
list(map(lambda name: name[0], names))

# to reverse the name
names = ['Andy', 'Eve', 'Sally']
list(map(lambda x : x[: : -1], names))   # function argument can be anything, here x
 

