from helper_functions import clear_screen
clear_screen()

# ==============
# INPUT FUNCTION
# ==============

'''
OVERVIEW
--------
You can use the print() function to output data to the terminal window.

If you want to get data from the user, you can use the input() function.

The argument you put into the input() function will display in the terminal.

The words that the user types in the terminal will be returned to your program
by the input() function, wherever you called it.
'''

# 1. GATHING INPUT FROM THE USER
# Ask the user what their favorite food is using the input() funciton. Add a
# colon and a space to the argument to make it look nice.
input("pls tell me ur favorite food: ")

# 2. STORE THE INPUT FROM A USER
# Do the same thing as above, but store the input in a variable, and then print
# it out.

favorite_food = input("pls tell me ur favorite food: ")
print(favorite_food)


'''
CONVERT ONE DATATYPE TO ANOTHER
-------------------------------
Let's say you have a variable x. You can use the following functions

int(x)	    Converts x to an integer
float(x)	Converts x to a floating-point number (decimals)
str(x)	    Converts x to a string
bool(x)     Converts x to a bool. Like 0 becomes False and 1 becomes True
'''

# 3. CONVERTING DATA
# Ask the user for their favorite number, store it in a variable
# Then, add 10 to that number and print it out. Notice the error you get
# Try making it work by converting your input into an integer.
fav_number = input("enter your favorite number: ")

# this doesn't work: 
# result = fav_number + 10
# print(result)

fav_number = input("enter your favorite number: ")

result = int(fav_number) + 10
print(result)

# or
fav_number = int(input("enter your favorite number: "))
