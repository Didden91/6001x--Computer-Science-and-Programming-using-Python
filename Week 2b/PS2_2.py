# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 00:38:37 2021

@author: Ivo
"""

balance = 3329
annualInterestRate = 0.2

monintrate = (annualInterestRate) / 12.0 
fixedmonpay = 0
monunpaidbal = 0
updatedbal = 0
requiredpay = 250

monthsinyear = 13
remainingmonths = 12
sum = 0


for months in range(1, monthsinyear):
    
    # requiredpay = balance / remainingmonths
    while requiredpay * remainingmonths < updatedbal:
        print('requiredpay * remainingmonths =', requiredpay * remainingmonths)
        print('balance:', balance)
        print('required pay @',requiredpay,' so too low')
        requiredpay += 10
        print('required pay now @',requiredpay)
    
    balance -= requiredpay
    
    
    monunpaidbal = balance - fixedmonpay
    ## interest is compounded AFTER monthly payment is made
    updatedbal = monunpaidbal + (monintrate * monunpaidbal)
    balance = updatedbal
    remainingmonths -= 1
    sum += requiredpay
    print('required payment:', requiredpay)
    
    
average = sum / 12
print('average:', average)
    

  while requiredpay < monthly unpaid balance / remaining months
