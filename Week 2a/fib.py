# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 23:07:59 2021

@author: Ivo
"""

def fib(x):
    # Assumes x an int >= 0
    # returns Fibonacci of x
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
print(fib(5))