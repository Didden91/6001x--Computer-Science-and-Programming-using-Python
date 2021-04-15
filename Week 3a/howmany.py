# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 01:13:08 2021

@author: Ivo
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    
    values = aDict.items()
    
    
    largest = 0
    for i in values:
        if len(i) > largest:
            largest = len(i)
            biggest = i
            
            
    
        # biggest = aDict.index(i)
        
    return biggest

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))