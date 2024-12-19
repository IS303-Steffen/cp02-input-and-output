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

# =====================================
# ESCAPE CHARACTER AND ESCAPE SEQUENCES
# =====================================

'''
OVERVIEW
--------
The backslash \ is the "escape character". It lets you insert special
characters into a string or use quotes without ending the string.

When combined with a recognized character, it forms an "escape sequence."

    \n  - Newline, like pressing Enter.
    \t  - Tab, like pressing Tab.
    \'  - Single quote, useful in single-quoted strings.
    \"  - Double quote, useful in double-quoted strings.
    \\  - Backslash, since \ is itself the escape character.
'''



# 1. USING THE NEWLINE ESCAPE SQUENCE
# In a single print() function, print out a message that looks like this:
'''
IS 201
IS 303
IS 110
'''



# 2. USING THE TAB ESCAPE SEQUENCE
# In a single print() function, print out a message that looks like this:
'''
My favorite foods:
    Chocolate
    A giant bag of Cheetos
'''


# 3. SINGLE QUOTE AND BACKSLASH ESCAPE SEQUENCES
# In a single print() function, with a string that starts with single quotes '
# print out a message that looks like this:
'''
Prof Steffen's favorite slash looks like this: \
'''
