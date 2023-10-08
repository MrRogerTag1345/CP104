"""
------------------------------------------------------------------------
This program provides measurement for the number of Serving of Mac and Cheese
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-09-21"
------------------------------------------------------------------------
"""

# Constants.
MILK = 4
BUTTER = 8
FLOUR = 0.5
SALT = 2
SERVING = 6

# Gets the input.
inpt = int(input("Enter servings of Mac & Cheese: "))

# Math variables.
v1 = inpt / SERVING
milk = v1 * MILK
butter = v1 * BUTTER
flour = v1 * FLOUR
salt = v1 * SALT

# Prints the output.
print(inpt, "servings of Mac & Cheese requires:")
print("milk (cups):", milk)
print("butter (tablespoons):", butter)
print("flour (cups):", flour)
print("salt (teaspoons):", salt)
