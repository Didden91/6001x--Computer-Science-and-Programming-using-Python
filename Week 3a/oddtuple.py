# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:42:19 2021

@author: Ivo
"""

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print(applyEachTo([inc, max, int], -3))