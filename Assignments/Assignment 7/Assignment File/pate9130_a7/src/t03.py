"""
------------------------------------------------------------------------
t03.py
This program finds the most used letter in the string.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-23"
------------------------------------------------------------------------
"""

# Import from functions.
from functions import find_frequent

# Input from the user.
var_one = input("Enter a string: ")

# Send to the function.
result = find_frequent(var_one)

# Print statement.
print("Most frequent characters: {}".format(result))
