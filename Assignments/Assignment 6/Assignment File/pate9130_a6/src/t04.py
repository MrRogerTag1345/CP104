"""
------------------------------------------------------------------------
t04.py
This program reverse's the list of positive number.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-15"
------------------------------------------------------------------------
"""

# Import from functions.
from functions import read_positive, reverse_list

# Calls on function read_positive for inputing in positive integers.
list = read_positive()

# This calls on the functions to reverse the list.
arr = reverse_list(list)

# Print the values in the list.
print("List entered:", list)
print("List reversed:", arr)

