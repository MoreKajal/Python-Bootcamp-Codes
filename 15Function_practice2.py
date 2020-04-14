# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:31:41 2020

@author: Kajal
"""

## Q1: Write a function that capitalizes first and fourth letterrs of name
def old_macdonald(name):
    first_letter = name[0]
    in_between = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    
    return first_letter.upper() + in_between + fourth_letter.upper()+ rest

old_macdonald('macdonald')

## OR
# Using capitalize method used to capitaliaze first letter of string
def old_macdonald(name):
    first_part = name[:3]
    second_half = name[3:]
    
    return first_part.capitalize() + second_half.capitalize()
old_macdonald('macdonald')

## Q2 : Given a sentence, return a sentence with words reversed
def master_yoda(mystring):
    wordlist = mystring.split()
    reversed_wordlist = wordlist[: : -1]
    return reversed_wordlist
    ## This returns a list of words but we need string output    

master_yoda('I am at home')

## So use join list as 
mylist = ['a', 'b', 'c']
' '.join(mylist)
' -- '.join(mylist)   ## We can pass anything inside the join 

## OR for master_yoda
def master_yoda(mystring):
    wordlist = mystring.split()
    reversed_wordlist = wordlist[: : -1]
    return ' '.join(reversed_wordlist)
master_yoda('I am at home')


## Q3 : Given an ibteger, return true if n is within 10 of eitherr 100 or 200
## Using absolute value method
def almost_there(n):
    return (abs(100 -n) <= 10 ) or (abs(200 - n ) <= 10)
almost_there(150)  ##  False
almost_there(209)  ## True

