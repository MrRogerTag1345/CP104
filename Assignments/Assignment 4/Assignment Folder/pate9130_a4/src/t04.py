"""
------------------------------------------------------------------------
t04.py
This program takes a number and finds the pocket which has a colour value
to it.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-10-25"
------------------------------------------------------------------------
"""

# Import from functions.
from functions import pocket_colour

# User input.
number = int(input("Enter a pocket number: "))

# Send input through functions.
result = pocket_colour(number)

# Output if statement for printing.
if result == "Error":
    print(result)
else:
    print("The selected pocket is {}".format(result))
