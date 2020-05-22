__author__ = 'Caroline Sun'
# draw gallows for Hangman project
# 2020-04-26

# CLASSIC
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# initial gallows

gallows_1 = '''
_______
|
|
|
|
|_____
|     |
-------

'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# gallows + noose

gallows_2 = '''
_______
|     |
|     
|
|
|_____
|     |
-------

'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# gallows + noose, head

gallows_3 = '''
_______
|     |
|     O
|
|
|_____
|     |
-------

'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# gallows + noose, head, body

gallows_4 = '''
_______
|     |
|     O
|     |
|
|_____
|     |
-------

'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# gallows + noose, head, body, 1 arm

gallows_5 = r'''
_______
|     |
|     O
|    /|
|
|_____
|     |
-------

'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# gallows + noose, head, body, 2 arms

gallows_6 = r'''
_______
|     |
|     O
|    /|\
|
|_____
|     |
-------

'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# gallows + noose, head, body, arms, 1 leg

gallows_7 = r'''
_______
|     |
|     O
|    /|\
|    /
|_____
|     |
-------

'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# gallows + noose, head, body, arms, 2 leg

gallows_8 = r'''
_______
|     |
|     O
|    /|\
|    /¯\
|_____
|     |
-------

'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

gallows_ver = [gallows_1, gallows_2, gallows_3, gallows_4, gallows_5, gallows_6, gallows_7, gallows_8]