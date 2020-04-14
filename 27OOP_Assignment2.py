# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:00:59 2020

@author: Kajal
"""

## Account balance

class Account():
    def __init__(self, owner, balance=0):
        
        self.owner = owner
        self.balance = balance
    
    def deposit(self, dep_amt):
        
        self.balance = self.balance + dep_amt
        print(f"Added {dep_amt} to the balance")
    
    def withdrawal(self, wd_amt):
        
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print("Withdrawal accepted")
        else:
            print("Sorry !  Not enough funds")
            
    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"
    
a = Account("Sam", 500)
print(a)

a.deposit(200)
print(a)

a.withdrawal(500)
