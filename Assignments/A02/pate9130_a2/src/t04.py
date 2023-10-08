"""
------------------------------------------------------------------------
t04.py
This program takes the number of available number of balloons and divides the number of balloons
equally among the number of children. If there are left over balloons they will not be distributed. 
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-10-03"
------------------------------------------------------------------------
"""

# User input.
balloons = int(input("Number of balloons: "))
children = int(input("Number of children: "))

# Compute the amount that should be distribute. 
var_one = balloons // children
var_two = balloons % children

# Print the output statement and what is in the variables. 
print("Each child will receive", var_one, "balloons")
print("Balloons that will not be distributed:", var_two)
