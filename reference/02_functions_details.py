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

# Note: I recommend starting to use the debugger now to get familiar with it.

# Functions
'''
functions are prewritten code that you are "calling".
in python, they always have parentheses
You give it an input, and it will do something with that input.
so far, we've seen type() and print()
'''
my_name = 'steffen'

print(my_name)
print(type(my_name))

'''
sometimes, functions can accept multiple inputs.
If so, they are separated by a comma.

Let's try it with print.
print out my_name, other_name, and another string not stored in a variable
all in one print function
'''

other_name = 'george'

print(my_name, other_name, "something else")

'''
Everything you put into a function is called an "argument" or a "parameter"
(we'll discuss the difference between "argument" and "parameter" more
once we write our own fuctions. For now don't worry about it)

Sometimes to access specific arguments, you need to name the parameter
for print() we can try naming the specific parameters of sep = "" and end =""
make sep= an underscore and end= a hashtag
'''

print(my_name, other_name, sep = "_", end="#")


'''
Some functions can come at the end of a variable or other function by using a period .
These are called methods (a specific type of function) most just still call them functions.
'''

# .upper() and .lower()
# use .upper() on the my_name variable and print it out
# note that using .upper() won't change the value of the text.

print(my_name.upper())
