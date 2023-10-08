"""
------------------------------------------------------------------------
t02.py
This program takes a sum of digits as a string and get the sum.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-23"
------------------------------------------------------------------------
"""

# Import from functions.
from functions import sum_digit

# User Input.
my_str = input("Enter numbers: ")

# Send to function.
total = sum_digit(my_str)

# Print the final statement.
print("{}".format(total))
