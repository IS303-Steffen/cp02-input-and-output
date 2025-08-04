from helper_functions import clear_screen
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
print("Bob has 20 dogs.")
num_dogs = int(input("How many dogs do you have? "))

difference = 20 - num_dogs

print(f"Bob has {difference} more dogs than you.")