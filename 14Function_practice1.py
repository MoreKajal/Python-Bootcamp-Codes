# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:55:21 2020

@author: Kajal
"""

## Q1 : Lesser of two numbers if both are even but 
# returns greater if one or both are odd

def lesser_of_two(a, b):
    if a % 2 ==0 and b%2 ==0:
        #Both are even
        if a <b:
            result = a
        else:
            result = b
    else:
        if a > b:
            result = a
        else:
            result = b
    return result
lesser_of_two(2,6)

## OR
def lesser_of_two(a, b):
    if a % 2 ==0 and b%2 ==0:
        #Both are even
        result = min(a, b)
    else:
        result = max(a, b)
    return result
#lesser_of_two(2,6)
lesser_of_two(5, 7)

## OR
# Instead of saving result each time and return back at the last
def lesser_of_two(a, b):
    if a % 2 ==0 and b%2 ==0:
        #Both are even
        return min(a, b)
    else:
        return max(a, b)
    
#lesser_of_two(2,6)
lesser_of_two(5, 7)

## Q2 : Animal cracker : Function takes a two word string and returns
# True if both words begin with same letter

def animal_cracker(mystring):
    letters_list = mystring.split()
    print(letters_list)
    
    first_l = letters_list[0]
    second_l = letters_list[1]
    
    if first_l[0] == second_l[0]:
        return True
    else:
        return False
    
animal_cracker('live life')

## OR
def animal_cracker(mystring):
    letters_list = mystring.split()
    
    return letters_list[0][0] == letters_list[1][0]

animal_cracker('crazy kangaroo')

## But this wont work for different letter cases
# So make the letters first lower-case and then split
def animal_cracker(mystring):
    letters_list = mystring.lower().split()
    
    return letters_list[0][0] == letters_list[1][0]

animal_cracker('crazy Kangaroo')


## Q3 : Makes 20 : returns true if sum of two integers is 20 
# or any one of them is 20 else return false

def makes_tewnty(n1, n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20 or n2 == 20:
        return True
    else:
        return False
    
makes_tewnty(10, 10)

## OR
def makes_tewnty(n1, n2):
    
    return (n1+n2) == 20 or n1 == 20 or n2 == 20
makes_tewnty(10, 10)



