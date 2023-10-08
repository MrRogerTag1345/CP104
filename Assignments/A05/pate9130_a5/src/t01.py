"""
------------------------------------------------------------------------
t01.py
This program takes a value and find perfect squares.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-07"
------------------------------------------------------------------------
"""

# Import.
from functions import perfect_square

# Input
square = int(input("Enter a positive number: "))

# Send results to function.
result = perfect_square(square)

# Print statement.
if (square < 0):
    print(result)
else:
    print("Perfect squares below {} are: {}".format(square, result))
