# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 00:12:11 2021

@author: Ivo
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monintrate = (annualInterestRate) / 12.0 
minmonpay = 0
monunpaidbal = 0
updatedbal = 0

monthsinyear = 13

for months in range(1, monthsinyear):
    minmonpay = monthlyPaymentRate * balance
    monunpaidbal = balance - minmonpay
    updatedbal = monunpaidbal + (monintrate * monunpaidbal)
    balance = updatedbal
    
print('Remaining balance:',round(balance,2))
    
    
    
    
    
    
    
    

