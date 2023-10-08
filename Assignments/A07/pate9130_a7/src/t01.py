"""
------------------------------------------------------------------------
t01.py
This program takes a students drivers test.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-21"
------------------------------------------------------------------------
"""

# Import from functions.
from functions import driver_license

# Constant List.
ANS = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]

# Input from the user.
var_one = input("Enter a sequence of 20 choices separated by a space, each A-D in Uppercase: ")
var_one = var_one.split()

# Send results into functions.
c_answers, i_answers, list_answers = driver_license(ANS, var_one)

# If statement checks if the user passed or not, and prints the output statement.
if c_answers >= 15:
    print("You passed your driver license exam")
else:
    print("You failed your driver license exam")

print("#Correct answers = {} ,#incorrect answers = {}".format(c_answers, i_answers))
print("A list of incorrectly answered questions = {}".format(list_answers))
print("To pass the exam you need to score 15 out of 20")
