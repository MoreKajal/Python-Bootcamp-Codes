# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 21:01:16 2020

@author: Kajal
"""

import datetime

time = datetime.time(5,25,1)
print(time)

datetime.time.min
datetime.time.max

# min and max reflects the time range
# Time class doesnt give day information

## Date representation
today = datetime.date.today()

print(today)    # 2020-04-11

today.timetuple()    # time.struct_time(tm_year=2020, tm_mon=4, tm_mday=11, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=102, tm_isdst=-1)
today.year
today.month
today.day

print(datetime.date.resolution)

d1 = datetime.date(2015, 3, 11)
print(d1)

# We can replce
d2 = d1.replace(year = 1995)
d2



