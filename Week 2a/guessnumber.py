# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 14:51:43 2021

@author: Ivo
"""
guess = 50

high = 100
low = 0

print("Please think of a number between 0 and 100!")



while True:
    
    print("Is your secret number",guess,"?")

    inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if inp == 'h':
        high = guess
        guess = (low + high) / 2
        guess = int(guess)

    elif inp == 'l':
        low = guess
        guess = (high + low) / 2  
        guess = int(guess)
    
    elif inp == 'c':
        print("Game over. Your secret number was:",guess)
        break
    else:
        print("Sorry, I did not understand your input.")
        

