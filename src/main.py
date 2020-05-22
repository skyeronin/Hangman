__author__ = 'Caroline Sun'

# Hangman project
# 2020-04-26

import time, random, re
from src.gallows import drawGallows

words: list
count: int = 0
choice: int = 0
guessWord: str = ''
computerGuess: str = ''
letterBlanks: list = []
lettersGuessed: list = []
whoPlays: list = ['computer', 'user']
hangmanStyle: list = ['classic', 'adventurous', 'modern']

with open('words.txt', 'r') as f:
    allWords = f.read().split("\n")


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
    # print(guessWord)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# draws guessing blanks

def drawBlanks(letterBlanks):
    ''' draws blanks to match length of random word '''

    print(' '.join(letterBlanks))
    print()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# redraw blanks

def updateDisplay(guessLetter, guessWord, userPlays):
    ''' redraws blanks once user guesses correctly '''
    global count

    # re/find method from -->   https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
    letterPositions = [m.start() for m in re.finditer(guessLetter, guessWord)]

    if not letterPositions:
        count += 1
        # print(count)

    for i in letterPositions:
        letterBlanks[i] = guessLetter

    if userPlays:
        drawGallows(choice, count)

    drawBlanks(letterBlanks)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# word guessed

def hasWon(userPlays):
    ''' True when player guesses all letters, false otherwise '''
    if userPlays:
        return "_" not in letterBlanks
    else:
        return len(allWords) == 1


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
# counts number of times a letter appears in word list

def computerCountLetters(letter):
    '''use filter method to count frequency:
    https://book.pythontips.com/en/latest/map_filter.html'''

    # number of words that have the letter
    return len(list(filter(lambda x: letter in x, allWords)))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# chooses most frequent letter in word file

def computerGetLetter():
    '''chooses letter with highest frequency:
    1. read word file
    2. find ASCII values from a-z: 97-122
    3. use countLetters to find counts, then find max
    '''

    global computerGuess
    frequencyCount = []

    for i in range(97, 123):
        if chr(i) in lettersGuessed:
            frequencyCount.append(0)
        else:
            frequencyCount.append(computerCountLetters(chr(i)))

    computerGuess = chr(frequencyCount.index(max(frequencyCount)) + 97)
    return computerGuess


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# chooses most frequent letter in word file

def computerUpdateList():
    '''computer chooses the letter found in getLetter, updates allWords list'''
    global allWords

    if not computerGuess:
        # you know the number of blanks, eliminate words with different length
        allWords = list(filter(lambda x: len(x) == len(letterBlanks), allWords))

    elif computerGuess in letterBlanks:

        # re/find method from -->   https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
        letterPositions = [m.start() for m in re.finditer(computerGuess, guessWord)]

        # x is the word in allWords, and y is the position in letterPositions
        # all() tests the letters in the positions & if they are computerGuess
        # if x is longer than guessWord, check only the positions in len(x)
        allWords = list(filter(lambda x: all(y < len(x) and computerGuess == x[y] for y in letterPositions), allWords))

    else:
        allWords = list(filter(lambda x: computerGuess not in x, allWords))

    print(allWords)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# main function

def main():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # choose hangman version
    global choice, count, letterBlanks, guessWord

    print('Welcome to HANGMAN!\n')
    print('Enter... \n')

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # choose computer or player
    for i, ptype in enumerate(whoPlays):
        print(f"{i}: {ptype}")
    print('\n__________________________________\n')
    while True:
        # getting choice of 0, 1
        try:
            userPlays = int(input('Enter your choice: '))
        except ValueError as e:
            # print(e)
            print('An integer from 0 to 1, please.\n')
            continue

        # sanitizing choice ints
        if userPlays > 1 or userPlays < 0:
            print('Try again, doofus.\n')
            continue

        # confirming choice
        time.sleep(0.4)
        print(f'\nThe {whoPlays[userPlays]} will guess!\n')
        time.sleep(1)
        break

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # choose mode of play
    if userPlays:
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
            time.sleep(0.4)
            print(f'\nYou have selected the {hangmanStyle[choice]} hangman game!\n')
            time.sleep(1)
            break

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # the actual game

    # import drawings of gallows based on choice

    if userPlays:
        importWords()
        getNewWord()
    else:
        while True:
            guessWord = input('Give me a word: ')
            if guessWord in allWords:
                break
            print("Sorry, I don't know that word. Another one?")

    letterBlanks = ['_'] * len(guessWord)

    if userPlays:
        drawGallows(choice, count)
    else:
        computerUpdateList()
    drawBlanks(letterBlanks)

    while not hasWon(userPlays):
        print("Letters guessed: ", sorted(lettersGuessed))

        guessLetter = input('Guess a letter: ') if userPlays else computerGetLetter()

        if validateInput(guessLetter):
            lettersGuessed.append(guessLetter)
            print()
            # time.sleep(1)

            updateDisplay(guessLetter, guessWord, userPlays)
            if not userPlays:
                computerUpdateList()

        if count >= 7 and userPlays:
            print("Game Over...")
            print("You couldn't save him!")
            break

    if hasWon(userPlays):
        print(f'Congratulations! You guessed the word, "{guessWord}," correctly in {len(lettersGuessed)} tries!')


if __name__ == '__main__':
    main()
    # testDraw()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
