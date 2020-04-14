# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:02:17 2020

@author: Kajal
"""

# defaultdict

from collections import defaultdict

d = {'k1':1}
d['k1']      # >> 1

# if we try to access a key which is not present in dict, will throw error

d = defaultdict(object)
d['one']    # >> <object at 0x6309f10>

for item in d:
    print(item)     # >> one
    
d = defaultdict(lambda: 0)

d['one']  # >> 0

d['two'] = 2

d       # It adds to the existing dictionary
        # Lambda returns 0 to the keys which has not assigned a value



