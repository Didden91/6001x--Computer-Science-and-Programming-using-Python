# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:28:24 2021

@author: Ivo
"""

def iterPower(base, exp):
    total = base
    if exp == 0:
        return 1
    for i in range(exp - 1):
        total *= base
    return total

# print(iterPower(-4.11, 6))



def recurPower(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * recurPower(base, exp - 1)
    
print(recurPower(-2.3,8))
