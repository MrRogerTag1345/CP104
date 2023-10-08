"""
------------------------------------------------------------------------
t11.py
This program formats which direction to print output.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-09-28"
------------------------------------------------------------------------
"""
# Constant Variables.
LOC_1 = "left"
LOC_2 = "middle" 
LOC_3 = "right"

# Print Statements.
print("{:-<20}".format(LOC_1))
print("{:-^20}".format(LOC_2))
print("{:->20}".format(LOC_3))
