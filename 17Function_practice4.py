# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:47:25 2020

@author: Kajal
"""

## Q1 : SPY Game: Write a function that takes in a 
# list of integers & return true if it contains 007 in order
# May not be in consecutive order

def spy_game(nums):
    code = [0,0,7, 'x']
    # The iterations after matching are
    #[0, 7,'x']
    #[7, 'x']
    #['x']   length = 1
    for num in nums:
        if num == code[0]:
            code.pop(0)
        
    return len(code) == 1

spy_game([1,7,2,0,4,5,0])   # False
spy_game([1,0,2,4,0,5,7])   # True
spy_game([1,2,4,0,0,7,5])   # True

## Q2 : Count primes :write a function that returns a prime number
# that exist upto and including a given number
# By convension we treat 0 & 1 as non-prime

def count_primes(num):
    if num < 2:
        return 0   # here checking 0, 1 and negative numbe
    # for 2 and greater
    # list to store prime numbers
    primes = [2]
    # Counter going upto the input num
    x = 3
    
    while x <= num:
        # check if x is prime
        
#        for y in range(3,x,2):  # prime number are divisible by 2, so step size is 2
        # OR
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    print(len(primes))
    
count_primes(100)

    