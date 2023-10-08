"""
------------------------------------------------------------------------
t04.py
This function prints and displays a pattern.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-08"
------------------------------------------------------------------------
"""

# Import from functions.
from functions import print_pattern

# User input
var_one = int(input("Enter a positive integer number: "))

# Runs loop until a positive number has been entered.
for i in range(100):
    # Checks if the number entered is positive.
    if (var_one <= 0):
        var_one = int(input("Enter a positive integer number: "))
    else:
        break

# Sends input through function.
result = print_pattern(var_one)
