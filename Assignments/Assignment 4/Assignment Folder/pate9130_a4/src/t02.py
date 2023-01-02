"""
------------------------------------------------------------------------
t02.py
This program converts a integer to a corresponding day.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-10-25"
------------------------------------------------------------------------
"""

# Import.
from functions import num_day

# Input from user.
number = int(input("Please enter a number between 1 and 7: "))

# Send input to functions.
days = num_day(number)

# If statement for printing a error message or printing days.
if days == "Error":
    print("The number {} corresponds to Error".format(number))
else:
    print("The number {} corresponds to {}.".format(number, days))
