"""
------------------------------------------------------------------------
t04.py

------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-09"
------------------------------------------------------------------------
"""

from functions import generate_integer_list

var_one = int(input("Number values to generate: "))
var_two = int(input("Low value range: "))
var_three = int(input("High value range: "))

value = generate_integer_list(var_one, var_two, var_three)

print(value)
