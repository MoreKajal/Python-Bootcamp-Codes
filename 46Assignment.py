# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:36:53 2020

@author: Kajal
"""

# Q1 : Convert 1024 to binary and hexadecimal

print(bin(1024))
print(hex(1024))

#Q2 : Round 5.23222 to two decimal places
round(5.23222, 2)

# Q3 : Check if every letter in the string is lower case

s = 'hello how are you Kajal, are you feeling okay?'
s.islower()    # False

# Q4 : How many times does 'w' show up in the string
s = 'wtywywtwyybwuwgwhghwgehwwwh jhhw'
s.count('w')

# Q5 : Find elements in set1 that are not in set2

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

set1.difference(set2)

# Q6 : Find all elements that are in either set
set1.union(set2)

# Q7 : Create dictionary {0:0, 1:1, 2:8, 3:27, 4:64} using list comprehension
{ x:x**3 for x in range(5)}

# Q8 : Reverse the list below:
l = [1,2,3,4]
l.reverse()
l

# Sort the list
l = [3,4,2,5,1]
l.sort()
l

