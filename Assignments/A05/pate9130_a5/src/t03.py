"""
------------------------------------------------------------------------
t03.py
This program determines if the inputed number is a prime number.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-08"
------------------------------------------------------------------------
"""

# Import from functions
from functions import is_prime

# Input from the user.
var_one = int(input("Enter a positive integer number: "))

# Compares if value is negative.
if (var_one < 0):
    print ("Error: you entered a negative number")
else:
    result = is_prime(var_one)
    # Determines if the result was True which would mean it is a prime number or other wise.
    if (result == True):
        print("{} is a prime number".format(var_one))
    
    else:
        print("{} is not a prime number".format(var_one))
    
