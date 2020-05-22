__author__ = 'Caroline Sun'

# draw gallows for Hangman project
# 2020-04-26

import src.gallows_classic, src.gallows_adventurous, src.gallows_modern


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# updates drawing of gallows during game

def drawGallows(choice, count):
    ''' updates gallows drawing when player guesses wrongly '''
    if choice == 0:
        print(gallows_classic.gallows_ver[count])
    elif choice == 1:
        print(gallows_adventurous.gallows_ver[count])
    else:
        print(gallows_modern.gallows_ver[count])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#