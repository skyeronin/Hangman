__author__ = 'Caroline Sun'

# Hangman project
# 2020-04-26

import time, random, re
from src.gallows import drawGallows

words: list
count: int = 0
choice: int = 0
guessWord: str
letterBlanks: list
lettersGuessed: list = []
hangmanStyle: list = ['classic', 'adventurous', 'modern']


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# open/import data

def importWords():
    ''' get words from words.txt file, store in global "words" list '''
    global words

    with open('words.txt', 'r') as f:
        words = f.read().split('\n')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# randomly select word

def getNewWord():
    ''' randomly choose word from "words" list for each game'''
    global guessWord

    guessWord = random.choice(words)
    print(guessWord)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# draws guessing blanks

def drawBlanks(letterBlanks):
    ''' draws blanks to match length of random word '''

    print(' '.join(letterBlanks))
    print()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# redraw blanks

def updateDisplay(guessLetter, guessWord):
    ''' redraws blanks once user guesses correctly '''
    global count

    # re/find method from -->   https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
    letterPositions = [m.start() for m in re.finditer(guessLetter, guessWord)]

    if not letterPositions:
        count += 1
        # print(count)

    for i in letterPositions:
        letterBlanks[i] = guessLetter

    drawGallows(choice, count)
    drawBlanks(letterBlanks)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# word guessed

def hasWon():
    ''' True when player guesses all letters, false otherwise '''


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# sanitize player input

def validateInput(guessLetter):
    ''' sanitize player input:
        1. length 1
        2. must be alpha character
        3. no repeats '''

    # isalpha method from -->  https://docs.python.org/3/library/stdtypes.html
    if not guessLetter.isalpha():
        print('Guess a letter, a LETTER.\n')
        time.sleep(1)
        return False

    elif len(guessLetter) != 1:
        print('One letter at a time, please!\n')
        time.sleep(1)
        return False

    elif guessLetter in lettersGuessed:
        print('You\'ve already guessed that one!\n')
        time.sleep(1)
        return False

    # if input is none of the above...
    return True


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# tests draw function

def testDraw():

    for i in range(3):
        for j in range(6):
            drawGallows(i, j)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# main function

def main():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # choose hangman version

    global choice, count, letterBlanks

    print('Welcome to HANGMAN!\n')
    print('Enter... \n')

    for i, ptype in enumerate(hangmanStyle):
        print(f"{i}: {ptype}")

    print('\n__________________________________\n')
    while True:

        # getting choice of 0, 1, 2
        try:
            choice = int(input('Enter your choice: '))
        except ValueError as e:
            # print(e)
            print('An integer from 0 to 2, please.\n')
            continue

        # sanitizing choice ints
        if choice > 2 or choice < 0:
            print('Try again, doofus.\n')
            continue

        # confirming choice
        time.sleep(1)
        print(f'\nYou have selected the {hangmanStyle[choice]} hangman game!\n')
        time.sleep(1.5)
        break

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # the actual game

    # import drawings of gallows based on choice

    importWords()
    getNewWord()

    letterBlanks = ['_'] * len(guessWord)

    drawGallows(choice, count)
    drawBlanks(letterBlanks)

    while not hasWon():
        print("Letters guessed: ", sorted(lettersGuessed))
        guessLetter = input('Guess a letter: ')

        if validateInput(guessLetter):
            lettersGuessed.append(guessLetter)
            print()
            time.sleep(1)

            updateDisplay(guessLetter, guessWord)


if __name__ == '__main__':
    main()
    # testDraw()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#