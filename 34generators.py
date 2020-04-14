# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:32:52 2020

@author: Kajal
"""


def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

create_cubes(10)

for x in create_cubes(10):
    print(x)
## Note : here wee are preserving only the last value and the formula to yield next value
    # No need to store the complete list in joint memory
    
## So for not to store list in memory will do:
def create_cubes(n):
    
    for x in range(n):
        yield x**3

for x in create_cubes(10):
    print(x)
## The yield just stores the formula

# To get it into a list
list(create_cubes(10))


## Creating Fibonoci sequence
def gen_fibon(n):
    
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+b
        
for number in gen_fibon(10):
    print(number)
    
    
## Generators main to functions : next and iter function
    
def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()
g            ## >> <generator object

print(next(g))    # >> 0
print(next(g))    # >> 1
print(next(g))    # >> 2
print(next(g))    # >> StopIteration 
                    ## As the range given is upto 3
                    
## Interesting to nite: We didnt get this same error in above for loop
    # As the for loop catches the error and stops the iteration
    
## iter function: automatically iterates through other objects
s = 'hello'
for letter in s:
    print(letter)

next(s)    # >> 'str' object is not an iterator
# Need to turn the string into a generator

s_iter = iter(s)
next(s_iter)

next(s_iter)
    
next(s_iter)

next(s_iter)

next(s_iter)
    
next(s_iter)     # >> StopIteration

