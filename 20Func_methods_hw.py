# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:35:34 2020

@author: Kajal
"""


## Q1 : Write a function to compute a volumn of sphere given ites radius
# vol of sphere = (4/3) pi r^3

def volumn(radius):
    return (4/3) * (3.14)*(radius ** 3)

volumn(14)

## Q2 : Write a function to check wether a number is in given range (inclusive of high and low)

def check(num, low, high):
    # Check if num is between hig hand low
    if num in range(low, high):
        print( "%s is in the range " %str(num))
    else:
        print('The number is out of range')
        
check(5, 1, 10)

## OR : if we just return a boolean true or  false 
def check_bool(num, low, high):
    return num in range(low, high)

check_bool(5,1, 10)

## Q3 : Write a function that accepts a string and calculate number of upper case letter and lower case letters

def find_cases(mystring):
    upper = 0
    lower = 0
    
    for chars in mystring:
        if chars.isupper():
            upper += 1
        elif chars.islower():
            lower += 1
        else:
            pass
    return upper, lower

mystring= 'Is this Working Fine'
find_cases(mystring)

## OR returning the result in key-value pair

def find_cases(mystring):
    d = {'upper' : 0, 'lower' : 0}
    
    for chars in mystring:
        if chars.isupper():
            d['upper'] += 1
        elif chars.islower():
            d['lower'] += 1
        else:
            pass
    print("Original string is :", mystring)
    print("No. of Upper case letters are :", d['upper'])
    print("No. of lower case letters are:", d['lower'])
    
find_cases('Is this Working Fine')

## Q4": function that takes a list and returns a new list with unique elements of the first list

def unique_list(sample_list):
    # create a empty list and append 
    unique_list = []
    for i in sample_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
sample_list = [1,1,1,1,2,2,2,3,3,3,3,4,4,4,4]
unique_list(sample_list)

## OR can us set
set(sample_list)   # >> {1, 2, 3, 4}

## Q5 : Python function to multiply all numbers in a list
def mul_items(items):
    total = items[0]
    for x in items:
        total *= x
    return total
mul_items([1,2,3,4])    # >> 24

## Q6 : function to check wether passed string is pallindrome or not
# pallindrome is a word that the same forward and backword eg:madam, nurses run

def palindrome(mystring):
    if mystring == mystring[: : -1]:
        print('Its palindrome')
    else:
        print('Its not')

palindrome('maham')

## OR
def palindrome(mystring):
    return mystring == mystring[: : -1]
palindrome('maham')

## Q7 : function to check whether a string is pangram or not
# Pangram are words or sentences containing every letter of the alphabet atleast once

import string

def ispangram(str1, alphabet = string.ascii_lowercase):
    alphabet = set(alphabet)
    return alphabet <= set(str1.lower())

ispangram('The quick brown fox jumps over the lazy dog')

string.ascii_lowercase  

