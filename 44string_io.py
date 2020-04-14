# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:42:43 2020

@author: Kajal
"""

import  io

message = 'This is just a normal string.'


# Use StringIO method to set as file object
f = io.StringIO(message)

f.read()

f.write(' Second line written to file like object')

f.seek(0)

f.read()

f.close()
