"""
------------------------------------------------------------------------
t02.py
This program takes integer and convert's it into a date.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-10-04"
------------------------------------------------------------------------
"""

# Constants.
CONSTANT_ONE = 10000
CONSTANT_TWO = 100

# Ask the user for input.
date_input = int(input("Enter a date in the format MMDDYYYY: "))

# Compute integer to a separate date. 
date_one = date_input // CONSTANT_ONE
date_two = date_input % CONSTANT_ONE
date_three = date_one // CONSTANT_TWO
date_four = date_one % CONSTANT_TWO

# Print output statement
print("{}/{:0>1}/{}".format(date_four, date_three, date_two))

