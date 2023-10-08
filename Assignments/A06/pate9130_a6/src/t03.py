"""
------------------------------------------------------------------------
t03.py
This program determines the largest odd number in a list.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-15"
------------------------------------------------------------------------
"""

# Import from functions.
from functions import read_positive, largest_odd

# Calls on function read_positive for inputing in positive integers.
list = read_positive()

# Calls on the functions to find the largest odd number.
odd = largest_odd(list)

# Print the values in the list.
print("List entered:", list)
print("Largest odd:", odd)

