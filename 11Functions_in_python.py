# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:34:34 2020

@author: Kajal
"""

def add_function(num1, num2):
    return num1+num2
result = add_function(3,5)
result

def name_function():
    '''
    DOCSTRING : Information about the function
    INPUT : no input...
    OUTPUT : Hello...
    '''
    print('Hello')
    
help(name_function)

def say_hello(name):
    return 'Hello' + name
res = say_hello(' Kajal')
res

# check the string contains 'dog'
def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False
dog_check('My dog ran away')

# OR
def dog_check(mystring):
    return 'dog' in mystring.lower()
dog_check('My dog ran away')

## PIG_LATIN word

def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word
pig_latin('apple')    # starting with vowel, add 'ay' at the end
pig_latin('word')     # Non vowel start--> first letter at last, add 'ay' at end




