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


# input

'''
when we want input from the user of the program, we can use input()

input()
    argument (the stuff in the parentheses):
        gets displayed to the user in terminal, kind of like printing

    returned value:
        after the user types something in the terminal, the input() function "returns"
        whatever was typed. You'll want to store that returned text in a variable.
        The returned variable is always a string, even if a number was typed out.
'''

# PRACTICE
# Ask the user what their favorite food is. Add a colon and a space to make it look nice


# PRACTICE 
# Ask the user what their favorite food is, then store it in a variable.
# Print out that variable



# 4.2
# DATA CONVERSION

# PRACTICE
# Ask the user for their favorite number, store it in a variable
# Then, add 10 to that number and print it out.




'''
    input() always returns a string data type
    you will need to convert it if you want 
    it to work with other ints or floats
'''

# Explicity convert (you need to call a function)
'''
    int(x)	    Converts x to an integer
    float(x)	Converts x to a floating-point number (decimals)
    str(x)	    Converts x to a string
    chr(x)	    Converts x to a character (we probably won't use this one, but try putting an int in here if you're curious)
    bool(x)     Converts x to a bool. Like 0 becomes False and 1 becomes True
'''

# Fix the code you wrote above to that it will actualy work
# note that you can convert the variable it is stored in, or wrap the int() function around the input()


# or


# IMPLICIT CONVERSION
'''
    sometimes, a function expects a certain data type, but when it is the wrong
    datatype it will convert it automatically for you.

    For example, print() expects its arguments to be strings.
    But if you just print an int, it will figure it out and convert it for you

'''
# print 10 using the print function




