# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 09:58:42 2020

@author: Kajal
"""

## Q1 : given a list of ints, return true if array contains a 3 next to a 3 somewhere

def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

has_33([3,1,3])    ## False
has_33([1,3,1,3])  ## False
has_33([1,3,3])    ## True

## OR
def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i:i+2] == [3,3]:    ## Using slicing
            return True
    return False

## Q2 : PAPER DOLL: Given a string, return a string where for every character in the original there are three characters¶


def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result

paper_doll('Hello')

## Q3 : BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST


def blackjack(a,b,c):
    
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'
    

blackjack(5,6,7)   # 18
blackjack(9,9,9)   # BUST
blackjack(9,9,11)  # 19


## Q4 :SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 
# and extending to the next 9 (every 6 will be followed by at least one 9). 
# Return 0 for no numbers.

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

summer_69([1, 3, 5])   # 9
summer_69([4, 5, 6, 7, 8, 9])  # 9, ignores from 6 after
summer_69([2, 1, 6, 9, 11])    # 14, ignores (6,9) and add rest
 




