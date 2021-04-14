# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 14:55:20 2021

@author: Ivo
"""

# Balance = total due

# totalyearlycosts = balance with interest


    
balance = 3926
annualInterestRate = 0.2

monintrate = (annualInterestRate) / 12.0 

monthlypayment = 250


remainingmonths = 12

totalyearlycosts = balance + ((monintrate * balance) * remainingmonths)
REMAININGcosts = totalyearlycosts
Orgbalance = balance
NEWbalance = balance

while REMAININGcosts > 0:
    print("TOP OF LOOP")
    print('remaining months:', remainingmonths)
    print('remainingcosts are:', REMAININGcosts)
    
    
    
    for months in range(1, 13):
        # HIER vind de betaling plaats 
        NEWbalance = (NEWbalance - monthlypayment)
        # dan rente er bij op resterend bedrag
        NEWbalance = NEWbalance + (NEWbalance * monintrate)  
        print('New balance (TOTAL COSTS REMAINING) after payment is:', NEWbalance)
        # Resterende kosten na betaling
        REMAININGcosts = NEWbalance + ((monintrate * NEWbalance) * remainingmonths)
        print('Remaining costs after interest:',REMAININGcosts)
        
    if REMAININGcosts > 0:
        monthlypayment += 10
        NEWbalance = balance
        
        print('upping monthly payment by 10, to:',monthlypayment)
        print('restarting')
    
        
        
        
      
        
        
    
        #DE CHECK: is monthlypayment nu groter of gelijk aan de =>  NIEUWE totalremaingcosts / maanden
      
        
        
            
    

print('ALL COSTS PAYED')
                                 
    # Decrease if payment too high (not sure if I need it anymore)          
    # if (monthlypayment * remainingmonths) - REMAININGcosts > 10:
    #     monthlypayment -= 10
    #     print('monthly payment too high, decreasing by 10, to:',monthlypayment)             
