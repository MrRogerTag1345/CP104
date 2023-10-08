"""
------------------------------------------------------------------------
t03.py
This program calculates the users federal and provincial tax from their
income.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-10-25"
------------------------------------------------------------------------
"""

# Import functions.
from functions import fed_tax
from functions import prov_tax

# Input from the user. 
income = int(input("Enter your income: $"))

# Send input through function. 
fed_return = fed_tax(income)
prov_return = prov_tax(income)

# Output print statement 
print("Federal tax:    ${:.2f}".format(fed_return))
print("Provincial tax: ${:>1.2f}".format(prov_return))
print("Total tax:      ${:.2f}".format(fed_return + prov_return))
