"""
------------------------------------------------------------------------
t06.py
This program computes the cost multiply by the quantity.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-09-28"
------------------------------------------------------------------------
"""

# Input from the user.
cost = float(input("Enter cost: $"))
quantity = int(input("Enter quantity: "))

# Compute to solve for final cost for the given price for quantity.
answer = cost * quantity

# Print output statement. 
print("Given a cost of ${:.2f} and a quantity of {} the total is ${:.2f}".format(cost, quantity, answer))
