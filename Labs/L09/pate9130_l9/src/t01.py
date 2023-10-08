"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-16"
------------------------------------------------------------------------
"""

from functions import is_hydroxide

chemical = input("Enter a chemical formula: ")

hydroxide = is_hydroxide(chemical)

print("{} is a hydroxide".format(chemical))
