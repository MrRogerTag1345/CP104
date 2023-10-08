"""
------------------------------------------------------------------------
t04.py
This program takes user input and calculates the height in meters from inches. Then prints answer on a sting.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-09-26"
------------------------------------------------------------------------
"""
# Constant variable.
INCHES = 39.37

# Input from the user. Then calculates math. 
var_one = int(input("Enter the height in inches: "))
var_two = float(var_one / INCHES)

# 
print("The equivalent height in meters is {:.2f}".format(var_two))

