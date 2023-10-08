"""
------------------------------------------------------------------------
t05.py
This program calculates a persons weighted exam mark form their mid term and
their final exam mark. 
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-10-04"
------------------------------------------------------------------------
"""
# Constants.
MIDTERM = 0.2
FINAL = 0.4

# Input statement from user. 
mid_mark = int(input("Midterm mark (%): "))
final_mark = int(input("Final exam mark (%): "))

# Compute the math.
exam_portion = ((MIDTERM * mid_mark) + (FINAL * final_mark)) / (FINAL + MIDTERM)

# Print the output statement.
print("Your weighted exam average is: {:.1f} %. The passing mark of the weighted exam average is 50%".format(exam_portion))
