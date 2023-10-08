"""
------------------------------------------------------------------------
t05.py
This program determines if the words are a chin or not.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-23"
------------------------------------------------------------------------
"""

# Import functions.
from functions import is_chain

# Defining variables.
list = []

# User input.
var_one = input("Enter words: ")

# Runs a loop until user enters a blank input.
while var_one != "":
    list.append(var_one)
    var_one = (input("Enter string: "))

# Sends results to the function.
result = is_chain(list)

# Print the final statement.
if(result == True):
    print("This string had a word chain")
else:
    print("This string did not have a word chain")
