# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 10:56:16 2020

@author: Kajal
"""

# What an object looks like in python
my_list = [1,2,3]
myset = set()

# Everything in python is object
type(myset)
type(my_list)

# Let's define a class :
# Class is basically a blueprint that defines the nature of a future object

class Sample():
    pass
my_sample = Sample()
type(my_sample)    ## __main__.Sample

## Now creating attribute 
class Dog():
    ## init is the method to creat instance, 
    ## always start with the self keyword which connects the method(in oop its func) to instance of class
    ## self allows to refer itself
    ## parameters are attributes ie some characteristics
    
    def __init__(self, breed):
        self.breed = breed
        
my_dog = Dog(breed = 'lab')
type(my_dog)    ## __main__.Dog 
my_dog.breed    ## 'lab'

# We thake in the argument
# Assign it using self.attribute_name
## We can take the attribute name, parameter name and actual value to pass may be same
class Dog():
    def __init__(self, mybreed, name, spots):
        self.my_attribute = mybreed
        self.name = name
        # Expect spots as booleans
        self.spots = spots
my_dog = Dog(mybreed='huskie', name = 'Sammy', spots= False)

type(my_dog)     ##  __main__.Dog  --> note type here is Dog
my_dog.my_attribute
my_dog.name
my_dog.spots         ## All these attributes are available at .tab



## Defining class object attribute
class Dog():
    # Class object attribute
    # Same for any instance of a class
    
    species = 'mammal'
    
    def __init__(self, mybreed, name, spots):
        self.my_attribute = mybreed
        self.name = name
        self.spots = spots
my_dog = Dog(mybreed='huskie', name = 'Sammy', spots= False)

type(my_dog)     ##  __main__.Dog  --> note type here is Dog
my_dog.my_attribute
my_dog.name
my_dog.spots  
my_dog.species   ## >>  'mammal'

