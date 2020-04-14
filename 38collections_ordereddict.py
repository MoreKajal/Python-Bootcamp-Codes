# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:14:41 2020

@author: Kajal
"""

#OrderedDict : it is a dictionary subclass that remembers the order in which its contents are added

d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

d   # Here might the order is not retained

from collections import OrderedDict

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5


#d = OrderedDict()
for k, v in d.items():
    print(k, v)
    
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1
 
print(d1 == d2)   # >> False

# If we just use normal dict ==> d1 == d2 is True


