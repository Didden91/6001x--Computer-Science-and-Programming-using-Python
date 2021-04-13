# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 22:22:34 2021

@author: Ivo
"""

def gcdIter(a, b):
    testvalue = 0
    if a > b : 
        testvalue = b
        for iter in range(b):
            
            if a % testvalue == 0 and b % testvalue == 0:
                return testvalue
            else:
                testvalue -= 1
    
    else: 
        testvalue = a
        for iter in range(a):
         
            if b % testvalue == 0 and a % testvalue == 0:
                return testvalue
            else:
                testvalue -= 1

            
    