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

from functions import count_frequency_value

fh = open("number.txt", "r")

value = int(input("Count"))

result = count_frequency_value(fh, value)

print(result)
