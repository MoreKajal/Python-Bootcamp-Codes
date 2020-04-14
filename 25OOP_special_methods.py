# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:46:52 2020

@author: Kajal
"""

mylist = [1,2,3]
len(mylist)

class Sample():
    pass

mysample = Sample()
print(mysample)   # Location of sample in memory
# while
print(mylist)     # Gives list in strins form

## Here comes special methods

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
b = Book('Python rocks', ' Kajal', 200)
print(b)      # it just says hey you have this book object in memory
              # Here the print function asks- what is the string representation of b
              
              
## So now if I try to transform b into string
## Hence defining a special methodrelated to string call
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
      
    def __len__(self):
        return self.pages
b = Book('Python rocks', ' Kajal', 200)
print(b)   ## >> Python rocks by  Kajal

len(b)   ## 200

## Now if you want to delete some method
del b

## Define a special method again 

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
      
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted")
        
b = Book('Python rocks', ' Kajal', 200)
print(b)

len(b)

del(b)

b   ## >> name 'b' is not defined

