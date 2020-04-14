# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:50:15 2020

@author: Kajal
"""

## Coding exercise

# Q1 : define a function that takes in string, returns a matching 
# where every even letter is uppercase and every odd letter is lowercase.


#def myfunc(mystring):
#    index_count = 0
#    result= " "
#    
#    for letter in mystring:
#        if index_count % 2 == 0:
#            result += letter.upper()
#        else:
#            result += letter.lower()
#        index_count += 1
#    print('The altered string is :', result)
#
#    
#
#myfunc(mystring)
#mystring = 'Hello there'

mystring = 'Hello there'
def myfunc(mystring):
    index_count = 0
    result= " "
    
    for letter in mystring:
        if index_count % 2 == 0:
            result += letter.upper()
#            print('what is here :', result)
        else:
            result += letter.lower()
        index_count += 1
    print('The altered string is :', result)

myfunc(mystring)
