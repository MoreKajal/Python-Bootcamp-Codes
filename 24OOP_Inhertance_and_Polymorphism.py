# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:12:57 2020

@author: Kajal
"""

## Inheritance : Form new classes from the classes that have already being use

class Animal():
    def __init__(self):
        print("Animal Created")
        
    def who_am_i(self):
        print("I am an Animl")
    
    def eat(self):
        print("I am eating")
        
my_animal = Animal()

## If now I want ta create a Dog class, lot of methods from Animal class are useful in Dog class

class Dog(Animal):     ## The class name "Animal" in parenthesis suggests that it is derived class from Animal
    def __init__(self):
        Animal.__init__(self)  ## Inheritance created
        print("Dog created")

my_dog = Dog()
my_dog.eat()

## If we want to overwrite a method
class Dog(Animal):     
    def __init__(self):
        Animal.__init__(self)  
        print("Dog created")
        
    def who_am_i(self):
        print("I am a Dog!")

my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()

## Polymorphism

class Dog():
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + " says Woof !"

class Cat():
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + " says Meow !"

nilo = Dog("niko")
felix = Cat("falix")

print(nilo.speak())

# Example of iteration of polymorphism

for pet in [nilo, felix]:
    print(type(pet))
    print(pet.speak())

## OR
def pet_speak(pet):
    print(pet.speak())

pet_speak(nilo)
pet_speak(felix)

## Abstract Method
class Animal():
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Dog(Animal):
    def speak(self):
        return self.name + " says meow!"

fido = Dog("Fido")
isis = Cat("Isis")
print(fido.speak())