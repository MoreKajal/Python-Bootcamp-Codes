# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:55:54 2020

@author: Kajal
"""

## Decorators

def func():
    return 1

func()

def hello():
    return "Hello!"
hello()

greet = hello
greet()     # here hello is assigned to greet

# Now if we delete hello, greet wont exxecute
del hello

hello()     # Error

greet()     # It still points to hello
# That is we are passing a function to other

## Lets see example of passing a  function within another function or calling function within other fuction
def hello(name = 'Jose'):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is the greet() function inside hello!'

hello()


## Passing a function inside other func
def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, before the original function')
        
        original_func()
        
        print('Some extra code, after the original function')
        
    return wrap_func

def func_needs_decorator():
    print('I want to be decorated!!')
    
func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)
decorated_func()

## Writing decorator

@new_decorator
def func_needs_decorator():
    print('I want to be decorated!!')

func_needs_decorator()   
# Here it executes all the inside functions
'''
Output is:
    func_needs_decorator()
Some extra code, before the original function
I want to be decorated!!
Some extra code, after the original function

'''



## Now  if we comment @new_decorator

#@new_decorator
def func_needs_decorator():
    print('I want to be decorated!!')

func_needs_decorator()

'''
Output is:
    func_needs_decorator()
I want to be decorated!!
'''

