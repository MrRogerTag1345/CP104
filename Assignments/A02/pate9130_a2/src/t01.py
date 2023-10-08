"""
------------------------------------------------------------------------
t01.py
This program calculate the annual profit for a company.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-10-04"
------------------------------------------------------------------------
"""

# Defining constants.
RATE = 0.23
RATE_IN_PERCENT = 23

# Input user statement. 
sales = int(input("Enter the total amount of sales: "))

# Compute the results.
profit = sales * RATE

# Print the header for the program
print("Projected Profit Report")
print("--------------------------")
print("Total sales:   $ {:.2f}".format(sales))
print("Annual profit: % {:}".format(RATE_IN_PERCENT))
print("--------------------------")
print("Profit:        $ {:}".format(profit))
