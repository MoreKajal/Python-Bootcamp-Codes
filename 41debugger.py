# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 21:10:56 2020

@author: Kajal
"""

# Python Debugger : Allow program execution step by step

import pdb
x = [1,2,4]
y = 2
z = 3

result = y+ z
print(result)

result2 = y + x
print(result2)      # Simple execution of this leads to type error

x = [1,2,4]
y = 2
z = 3

result = y+ z
print(result)

pdb.set_trace()

result2 = y + x
print(result2)     # After execution of this in ipdb> check the values
                    # press 'q' to quit

  
