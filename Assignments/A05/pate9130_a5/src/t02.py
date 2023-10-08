"""
------------------------------------------------------------------------
t02.py
This program takes a integer and get the factorial number from that value.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-07"
------------------------------------------------------------------------
"""

# Import from function.
from functions import factorial

# Input from the user.
var_one = int(input("Enter a positive number: "))

# Compares and prints results.
if (var_one < 0):
    print("Error: you entered a negative number")
else:
    # Send results to function.
    result = factorial(var_one)
    print("{}! = {}".format(var_one, result))
