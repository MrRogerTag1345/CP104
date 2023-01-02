"""
------------------------------------------------------------------------
t05.py
This program determines which team is going to win, which is given from
the user.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-08"
------------------------------------------------------------------------
"""

# Import from functions
from functions import winner

# Call on the function.
red, green = winner()

# If Statement determines the winner and prints message
if (red == green):
    print("tie")
elif (red > green):
    print("red wins")
else:
    print("green wins")
