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

# ========
# PRACTICE
# ========

# 1. PRACTICE
# Print out: "Bob has 20 dogs."
# Ask the user: "How many dogs do you have? "
# Then print out "Bob has x more dogs than you"
# with x being the difference between 20 and the number entered (just assume
# that you'll always put a number 20 or below)
