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

# ==================
# INTRO TO FUNCTIONS
# ==================

'''
OVERVIEW
--------
Functions are prewritten code. There's a lot to learn about them, and
eventually we'll make our own functions.

Usually, you provide an input to the function, called an argument. Then the 
function does something to your argument (like print it out in the terminal)

You put the arguments (the inputs) to the function in the parentheses. When you
use a function, the term is "calling". So if you use the print() function,
you are "calling" the print function.

'''

'''
Note
----
I recommend starting to use the debugger now to get familiar with it.
'''

# 1. CALLING THE PRINT FUNCTION
# Create a variable to hold your name. Call the print function using your name
# as an argument (the input). Call the type function as well.
my_name = 'steffen'
print(my_name)


# 2. CALL THE TYPE FUNCTION
# Call the type function without printing it. What happens? Many functions
# "return" a value when you run them. Try storing the result (the returned)
# value of the type() function in a new variable. And print that out.
# Then try just printing out the result of the type function without storing
# it in a new variable.
type_of_variable = type(my_name)
print(type_of_variable)

print(type(my_name))


'''
MULTIPLE ARGUMENTS (INPUTS)
---------------------------
Some functions let you enter multiple arguments (inputs) into the function.
Each argument needs to be separated by a comma

'''

# 3. USING MULTIPLE ARGUMENTS (INPUTS) WITH PRINT
# Create another string variable and print it out. Try adding some more text
# to the print function without storing it in a variable first.

other_name = 'george'

print(my_name, other_name, "something else")

'''
SPECIFYING PARAMETERS
---------------------
Sometimes you want to change the behavior of the function. Many functions
include extra "parameters". If you name the parameters, and provide them with
arguments, you can alter how the function... functions.

If you hover over a function name, you can see details about the different
parameters. Sometimes it will show explanations about the function too.

Don't worry about understanding everything you see yet. It will make more sense
over the course of the semester
'''


# 4. ALTER PARAMETERS IN THE PRINT FUNCTION
# Print out multiple strings like before using print(). However, after the 
# strings, alter the "sep" paremeter. What does it do?
# Try altering the "end" parameter. What does it do?

print(my_name, other_name, sep = "_", end="#")
print()

'''
METHODS: SPECIAL FUNCTIONS THAT START WITH "."
--------------------------------------------
Some functions only work once you have an existing variable of a specific
data type.

To use them, you add . after the variable and then the function name.

We'll learn a lot more about the difference between regular functions and
methods later on in the semester.
'''

# 5. USE THE UPPER() and LOWER() FUNCTIONS
# Add the .upper() function onto your name variable and print it out. Try doing
# the same thing with the .lower() function

print(my_name.upper())
print(my_name.lower())
