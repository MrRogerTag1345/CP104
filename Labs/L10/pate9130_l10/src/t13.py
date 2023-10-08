"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-23"
------------------------------------------------------------------------
"""

# Imports
from functions import file_copy
# Constants

# Inputs
fh_1 = open("words.txt", "r")
fh_2 = open("new_worlds.txt", "w")
# Calculations
file_copy(fh_1, fh_2)
# Outputs
print("Copying 'words.txt' to 'new_worlds.txt'")
fh_1.close()
fh_2.close()
