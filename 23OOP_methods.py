# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:59:05 2020

@author: Kajal
"""

class Dog():
    # Class object attribute
    # Same for any instance of a class
    
    species = 'mammal'
    
    def __init__(self, mybreed, name):
        self.my_attribute = mybreed
        self.name = name
        
    # Methods : Operations / Actions
    def bark(self):
        print("WOOF ! My name is  {}".format(self.name))
my_dog = Dog('huskie',  'Sammy')

type(my_dog)    
my_dog.my_attribute
my_dog.name
my_dog.species 
my_dog.bark()


## Methods can take outside arguments

class Dog():
    # Class object attribute
    # Same for any instance of a class
    
    species = 'mammal'
    
    def __init__(self, mybreed, name):
        self.my_attribute = mybreed
        self.name = name
        
    # Methods : Operations / Actions
    def bark(self, number):
        # Here number is not using self. as it is not referncing something, its user provided
        print("WOOF ! My name is  {} and the number is {} ".format(self.name, number))
my_dog = Dog('huskie',  'Sammy')

type(my_dog)    
my_dog.my_attribute
my_dog.name
my_dog.species 
my_dog.bark(10)



class Circle():
    # Class object attribute
    pi = 3.14
    
    def __init__(self, radius= 1):
         
         self.radius = radius
         self.area = radius * radius * self.pi
         
    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2
    
my_circle = Circle(30)    # Default is overwritten
my_circle.get_circumference()
my_circle.pi
my_circle.radius
my_circle.area
