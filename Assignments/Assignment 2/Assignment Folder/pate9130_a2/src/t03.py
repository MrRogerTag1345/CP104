"""
------------------------------------------------------------------------
t03.py
This program take a double digit number and sum's the the first and second term.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-10-04"
------------------------------------------------------------------------
"""
# Constant value.
CONVERT = 10

# Input double digits from user.
num_n = int(input("Enter a number: "))

# Compute the math.
var_one = num_n % CONVERT
var_two = num_n // CONVERT
var_three = var_one + var_two

# Prints the output.
print("The sum of the two numbers is", var_three)

