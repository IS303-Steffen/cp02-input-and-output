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


'''
In chapter 3 we went over documentation, variables and data types
'''

# Practice:
# make a variable to store your age, then a variable to store a sibling or parents age.
# subtract the two and print it out.
