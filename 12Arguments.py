# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 13:52:53 2020

@author: Kajal
"""

## Arguments and Keyword-Arguments
# By using *args wee can pass arbitrary no. of parameters

def myfunc(a, b,c=0,d=0,e=0):
    return sum((a,b,c,d,e) )

#myfunc(10,20,30,40,50)
myfunc(10,20,30,40,50, 60)   #For parameters greater than 5 it gives type error

# Here comes *args : it can take arbitrary no.of parameters 
def myfunc(*args):
    return sum(args)
    
#myfunc(10,20)
myfunc(50,40,30,80,90,50)    # Can pass many parameters
print(myfunc)

## *args type is tuple : explained below
def myfunc(*spam):        # * is the main operator
    for item in spam:     #the std practice is to use args(its random arguments)
        print(type(item))
myfunc(10,20,30)
       
#**kwargs returns a dictionary
def myfunc(**kwargs):
    print('what is kwargs :', kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
myfunc(fruit= 'apple', veggie = 'lettuce')  ## here if fruit key is not present, throws error 
 # But for many keys other than fruit it doesn't complain
 
 
def myfunc(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))
myfunc(10,20,30, fruit='orange', food='eggs', animal='dog')


        