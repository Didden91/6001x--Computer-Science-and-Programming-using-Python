# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 22:53:30 2021

@author: Ivo
"""

def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
        
print(gcdRecur(9, 12))
    