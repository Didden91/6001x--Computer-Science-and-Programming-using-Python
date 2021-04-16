# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import time

language = input('English (e), Nederlands EASY (n), of Nederlands ALLES (a):\n')
lang = language.lower()

if lang == 'e':
    time.sleep(1)
    print('You have chosen English.')
    WORDLIST_FILENAME = "words.txt"

elif lang == 'n':
    time.sleep(1)
    print('Je hebt gekozen voor Nederlands EASY.')
    time.sleep(1)
    print('Er wordt gekozen uit een lijst van 999 veel voorkomende Nederlandse woorden')
    time.sleep(1)
    print('Succes!')
    WORDLIST_FILENAME = "woordenEASY.txt"

elif lang == 'a':
    time.sleep(1)
    print('Je hebt gekozen voor Nederlands ALLES.')
    time.sleep(1)
    print('Er wordt gekozen uit een lijst van 189.892 Nederlandse woorden...')
    time.sleep(1.5)
    print('Ja echt, 189.892 Nederlandse woorden...')
    time.sleep(1)
    s = '189.892 woorden.......'
    for l in s:
        print(l, end='', flush=True)
        time.sleep(0.1)
    print()
    s2 = 'Good luuuuuuuuuuuuuck.....'
    for l in s2:
        print(l, end='', flush=True)
        time.sleep(0.07)
    print()
    WORDLIST_FILENAME = "woordenHARD.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    guessed = False
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed = True
            continue
        else:
            guessed = False
            break
    return guessed




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    returnlist = list('_'*len(secretWord))
    dicofletters = dict()

    count = 1
    for letter in secretWord:
        toaddtodic = {count:letter}
        dicofletters.update(toaddtodic)
        count += 1

    for letter in lettersGuessed:
         if letter in secretWord:

             for key in dicofletters:
                 if dicofletters[key] == letter:
                     #de key die hier uitkomt is de locatie van de letter
                     letpos = key - 1
                     returnlist[letpos] = letter

    returnstring = " ".join(returnlist)
    return returnstring




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    all_letters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in all_letters:
            all_letters.remove(letter)

    availableletters = " ".join(all_letters)
    return availableletters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = list()
    remainingguesses = 8
    availableLetters = getAvailableLetters(lettersGuessed)
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is',len(secretWord),'letters long.')
    print('-------------')

    ## NEW TURN
    while isWordGuessed(secretWord, lettersGuessed) == False:

        print('You have',remainingguesses,'guesses left.')
        availableLetters = getAvailableLetters(lettersGuessed)
        print('Available letters:',availableLetters)
        inp = input('Please guess a letter: ')
        guess = inp.lower()
        lettersGuessed.append(guess)
        if guess not in availableLetters:
            print('Oops! You\'ve already guessed that letter:',getGuessedWord(secretWord, lettersGuessed))
        elif guess in secretWord:
            print('Good Guess:', getGuessedWord(secretWord, lettersGuessed))
        else:
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            remainingguesses -= 1
        print('-------------')

        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')

        if remainingguesses == 0:
            print('Sorry, you ran out of guesses. The word was %s.' % secretWord)
            break






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist)
hangman(secretWord)
