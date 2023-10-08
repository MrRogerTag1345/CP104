"""
------------------------------------------------------------------------
This program outputs the profits of the day for each dog groomed.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-09-21"
------------------------------------------------------------------------
"""

# Determining the constants. 
L = 75
S = 50

# Ask the user for input.
l_vone = int(input("Number of large dogs groomed: "))
s_vone = int(input("Number of small dogs groomed: "))

# Math variable.
ans = float(l_vone * L + s_vone * S)

# Prints string and the response answer. 
print("Total earned for the day:$", ans)
