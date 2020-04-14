# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:46:24 2020

@author: Kajal
"""

# Counter : dictionary subclass use to count objects

from collections import Counter

# elements as key and values as value

l = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5]
Counter(l)

s = 'aaaasdduhjnnbbghghgghghhhhjmjmjkk'
Counter(s)

# Count of wordds repeated in a string
s = ' how many times does each word show up in this sentence word word show up up show'
words = s.split()
Counter(words)

c = Counter(words)

c.most_common(3)

## Common patterns when using the Counter() object

sum(c.values())  ## >> 17

c.clear()   # To reset all counts

list(c)     # List of unique elements

set(c)      # COnvert to set

dict(c)     # Convert to regular dictionay

c.items()   # Convert to list of (elem, cnt) pairs

Counter(dict(list_of_pairs))

c.most_common()[: -n-1 : -1] # n least common elements

c += Counter()      # remove zero and negative counts
