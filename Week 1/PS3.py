# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 18:11:00 2021

@author: Ivo
"""

s = 'azcbobobegghakl'

alphindex = 'abcdefghijklmnopqrstuvwxyz'



current = -1
reeks = ''
record = ''
for letter in s:
    thisletter = alphindex.find(letter)
    if thisletter >= current:
        reeks = reeks + letter
        current = thisletter
        if len(reeks) > len(record):
            record = reeks
    else:
        reeks = letter
        current = alphindex.find(letter)
        
print('Longest substring in alphabetical order is:',record)
        
        
        
   
        
    