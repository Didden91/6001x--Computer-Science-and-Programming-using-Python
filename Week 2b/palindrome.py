# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 23:13:03 2021

@author: Ivo
"""

s = 'abbasdasdfa'
def isPalindrome(s):
    
    def converttosimplechars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    
    def isPal(s):
        if len (s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(converttosimplechars(s))

print(isPalindrome(s))

