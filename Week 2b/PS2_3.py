# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 18:22:03 2021

@author: Ivo
"""
balance = 999999
annualInterestRate = 0.18

monintrate = (annualInterestRate) / 12.0 

monthlypayment = 0

monpaylowerbound = balance / 12
monpayupperbound = (balance * (1 + monintrate)**12) / 12.0
remainingmonths = 12

totalyearlycosts = balance + ((monintrate * balance) * remainingmonths)
REMAININGcosts = totalyearlycosts
Orgbalance = balance
NEWbalance = balance
monthlypayment = (monpaylowerbound + monpayupperbound) / 2 

while REMAININGcosts != 0:
   
     
    
    for months in range(1, 13):
        
        NEWbalance = (NEWbalance - monthlypayment)
        
        NEWbalance = NEWbalance + (NEWbalance * monintrate)  
        
        REMAININGcosts = NEWbalance + ((monintrate * NEWbalance) * remainingmonths)
        
    if round(REMAININGcosts, 2) == 0.01:
        break
    if REMAININGcosts > 0.01:
        print("Monthly payment TOO LOW")
        print('Average of two bounds becomes new LOWER bound')
        monpaylowerbound = (monpaylowerbound + monpayupperbound) / 2
        print('current monthlypayment:',monthlypayment)
        monthlypayment = (monpaylowerbound + monpayupperbound) / 2
        print('changing to:', monthlypayment)
        NEWbalance = Orgbalance
        REMAININGcosts = totalyearlycosts
        
    if REMAININGcosts < 0.01:
        print("Monthly payment TOO HIGH")
        print('Average of two bounds becomes new UPPER bound')
        monpayupperbound = (monpaylowerbound + monpayupperbound) / 2
        print('current monthlypayment:',monthlypayment)
        monthlypayment = (monpaylowerbound + monpayupperbound) / 2
        print('changing to:', monthlypayment)
        NEWbalance = Orgbalance
        REMAININGcosts = totalyearlycosts
    
        
       
print('Lowest Payment:',round(monthlypayment, 2))