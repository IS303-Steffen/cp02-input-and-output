import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# ======
# REVIEW
# ======

'''
OVERVIEW
--------
Previously, we went over documentation, variables and data types.
This is a very brief review of that.
'''

# 1. REVIEW
# Make a variable to store your age, then a variable to store a sibling or
# parents age. Subtract the two and print it out.
