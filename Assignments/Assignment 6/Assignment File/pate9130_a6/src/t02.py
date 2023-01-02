"""
------------------------------------------------------------------------
t02.py
This program find the target value in the list of positive numbers.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-15"
------------------------------------------------------------------------
"""

# Import from functions.
from functions import read_positive, find_target

# Calls on function read_positive for inputing in positive integers.
list = read_positive()

# Print the values in the list.
print("List entered:", list)

# Ask the user for the target number.
var_one = int(input("target = "))

# Call on the function to find the target value.
arr = find_target(list, var_one)

# Print final output.
print("target exists at location", arr)

