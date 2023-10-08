"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-23"
------------------------------------------------------------------------
"""
  # Imports
from functions import customer_append

# Constants

# Inputs
fields = ['35612', 'David', 'Brown', 237.56, '2008-10-10']
print("Data: {}".format(fields))             
fh = open("customers.txt", "a", encoding="utf-8")

# Calculations
customer_append(fh, fields)
fh.close()
