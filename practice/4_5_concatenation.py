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

# concatenation
'''
    concatenation just means combining two pieces of data together in a string

    2 main ways to do it:
        1. with +
        2. using f-strings (recommended)

    Also, a sort of 3rd way if you are using print()
        3. use commas in print()
'''


# traditional way, using +
# used in most languages.
# Annoying thing is you need to explicitly convert any non string data.

# PRACTICE
# print out first_name and last_name with a space between them. Use + to concatenate
first_name = "Jimmy"
last_name = "John"



# 3rd way, using commas in print

# PRACTICE
# do the same thing, but use commas in the print function instead.


# PRACTICE
age = 21
# do the same as before, but concatenate the age, so it says: "Jimmy John's age:21"



# 2nd way: f-strings (HIGHLY RECOMMENDED TO USE THIS)
# PRACTICE:
# write out Jimmy John's age:21" but using f-string


# PRACTICE
# Ask how many dogs you have.
# add 2 to the number
# Then print out: "You have this many dogs + 2: x"




