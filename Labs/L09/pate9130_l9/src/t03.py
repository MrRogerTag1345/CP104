"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-16"
------------------------------------------------------------------------
"""

from functions import parse_code

product_code = input("Enter a product code: ")

pc, pi, pq = parse_code(product_code)

print("Category:  ", pc)
print("ID:        ", pi)
print("Qualifier: ", pq)
