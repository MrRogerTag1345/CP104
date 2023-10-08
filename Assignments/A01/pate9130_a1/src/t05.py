"""
------------------------------------------------------------------------
t05.py
This program calculates the users compound interest over a certain time
period of the users choosing.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-09-25"
------------------------------------------------------------------------
"""

# Input from the user, stored in variables.
principal = int(input("Principal: "))
rate = float(input("Interest (decimal): "))
years = int(input("Number of years: "))
compound = int(input("Compound interest per year: "))

# Math variable. This calculates the compound interest.
balance = float(principal * ((1) + (rate / compound)) ** (compound * years))

# Prints string and the balance output
print("Balance: {:.2f}".format(balance))

