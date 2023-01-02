"""
------------------------------------------------------------------------
t01.py
This program calculates the production amount for the company.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-10-25"
------------------------------------------------------------------------
"""

# Import functions.
from functions import pieces_produced

# Input from the user.
time_of_day = int(input("Time of the day: "))
workers = int(input("Number of workers: "))

# Send results to functions.
result = pieces_produced(time_of_day, workers)

# If statement for printing the results.
if (result == -1):
    print("Can not perform the calculation")
else:
    print("The total number of pieces produced:{}".format(result))
