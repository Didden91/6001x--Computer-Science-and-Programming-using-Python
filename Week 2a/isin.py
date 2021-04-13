# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 23:22:53 2021

@author: Ivo
"""

s = 'abcdefgpqrtvz'

def isIn(char, aStr):
    
    if len(aStr) <= 1:
        stringmid = aStr
    else:
        stringmid = aStr[int(len(aStr)/2)]
    
    if len(aStr) <= 1 and char != stringmid:
        return False
    if char == stringmid:
        return True
    if char > stringmid:
        return isIn(char, aStr[int(len(aStr)/2):])
    if char < stringmid:
        return isIn(char, aStr[:int(len(aStr)/2)])        
         
    
print(isIn('x', s))