"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-09"
------------------------------------------------------------------------
"""

from functions import list_stats

values = [94, 96, -22, -79, -28, -26, -50, 71, 24, -32]
print(values)

v1, v2, v3, v4 = list_stats(values)

print("smallest value:", v1)
print("largest value:", v2)
print("total:", v3)
print("average:", v4)
