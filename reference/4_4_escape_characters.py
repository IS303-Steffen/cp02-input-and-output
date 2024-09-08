# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################



# Escape Characters
##

'''
    use a backslash to enter in special characters in strings. These are called "escape characters"
    They have two uses:
        1. write special characters like a tab or a new line:
            \n is a new line
            \t is a tab
        2. write characters that normally would show you are ending the line:
            \' this is useful if you are doing a string with single quotes. 
            \" useful if you are doing a string with double quotes
            \\ since backslash is the start of an escape character, if you put 2 then it prints out as 1
'''

# PRACTICE
# Print out a message that has your name, then another name, then another name, separated by new lines. Use \n
print('Your name\nanother name\nthen another name')


# PRACTICIE
# print out a message that says name 1, a tab, then a backslash, then another tab, then name 2.
# then a new line, then name 3, a tab, a backslash, then a tab, then name 4
print('name1\t\\\tname2\nname3\t\\\tname4')