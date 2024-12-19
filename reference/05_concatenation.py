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

# =============
# CONCATENATION
# =============

'''
OVERVIEW
--------
Concatenation combines two or more pieces of data into one string.

Main methods:
    1. + : Use the + operator to combine strings.
    2. f-strings: Use f-strings for easier and cleaner formatting.

Bonus method:
    3. Commas in print(): Combine items with commas in print().
'''

# 1. CONCATENATION USING +
# Print out first_name and last_name with a space between them. Use + to
# concatenate
first_name = "Jimmy"
last_name = "John"

print(first_name + " " + last_name)


# 2. CONCATENATION USING COMMAS IN PRINT
# Do the same thing as above, but use commas in the print function instead.
print(first_name, last_name)

# 3. CONCATENATION USING +, WITH DIFFERENT DATA TYPES
# Do the same as before, but concatenate the age, so it says:
# "Jimmy John's age: 21"
age = 21
print(first_name + " " + last_name + "'s age:" + str(age))


'''
F-STRINGS
---------
f-strings are a (somewhat) newer way to concatenate and format strings,
introduced in version 3.6.

They are easier to write, read, and faster for Python to run. Plus, you don't
need to convert data types. You should almost always use them.

name_example = "Jimmy"
string_example = f"My name is {name_example}"
'''

# 4. CONCATENATION WITH F-STRINGS (HIGHLY RECOMMENDED TO USE THIS)
# Write out Jimmy John's age: 21" but using f-string
print(f"{first_name} {last_name}'s age: {age}")


