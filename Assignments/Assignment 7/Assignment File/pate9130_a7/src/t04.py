"""
------------------------------------------------------------------------
t04.py
This program takes a non spaced string and adds spaces and puts them in lowercase.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-23"
------------------------------------------------------------------------
"""

# Import from functions.
from functions import add_spaces

# Get user input.
my_str = input("Enter a string: ")

# Send to the functions.
new_str = add_spaces(my_str)

# Print statement.
print(new_str)
