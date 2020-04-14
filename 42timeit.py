# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:48:13 2020

@author: Kajal
"""

# Timing your code

import timeit

'0-1-2-3-4-...................-99'

"-".join(str(n) for n in range(100))

timeit.timeit('"-".join(str(n) for n in range(100))', number = 1000)

# Add [] bracket to make it list comprehension
timeit.timeit('"-".join([str(n) for n in range(100)])', number = 1000)
# Notice that it is little faster

# Using map 
timeit.timeit('"-".join(map(str, range(100)))', number = 1000)

# magic function(%)
# No need to pass string

%timeit "-".join(str(n) for n in range(100))
# >> 43.3 µs ± 3.46 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
# It gives number of loops repeated and best of 3 time avg

%timeit "-".join(map(str, range(100)))


