"""
------------------------------------------------------------------------
t05.py
This program mixes two primary colours together.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-10-25"
------------------------------------------------------------------------
"""

# Import.
from functions import colour_mix

# Input from user.
colour_one = input("Enter a first colour: ")
colour_two = input("Enter a second colour: ")

# Input to the functions file.
mix_colour = colour_mix(colour_one, colour_two)

# If statement for printing.
if (mix_colour == "Error"):
    print("The mixed colour is Error")
else:
    print("The mixed colour is {}".format(mix_colour))
