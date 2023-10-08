"""
------------------------------------------------------------------------
This program takes input for the number of flyers, and the volunteers 
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-09-21"
------------------------------------------------------------------------
"""

# Get the input form the user.
var_one = int(input("Number of flyers: "))
var_two = int(input("Number of volunteers: "))

# Computes the math.
ma = var_one // var_two
ma2 = var_one % var_two

# Prints the string and the answers.
print("Flyers per volunteer", ma)
print("Flyers left over:", ma2)
