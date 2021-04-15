# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 01:59:55 2021

@author: Ivo
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    
    dicitems = aDict.items()
    
    largest = 0
    for key, values in dicitems:
        if len(values) > largest:
            largest = len(values)
            biggest = key
            
      
        
    return biggest

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))