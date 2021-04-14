# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 16:45:15 2021

@author: Ivo
"""
# ITERATION vs RECURSION
#For getting a factorial or ! of a number
#(factorial 4! for example = 1*2*3*4 = 24)

#Iteration: 
    
def factorial_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod = prod * i
    return prod

#Recursion:

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print('Iteration:',factorial_iter(4))
print('Recursion:',factorial(4))        

