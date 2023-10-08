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

from functions import customer_record

fh = open("customers.txt", "r")

n = int(input("Enter record number: "))

result = customer_record(fh, n)

fh.close()

print(result)

