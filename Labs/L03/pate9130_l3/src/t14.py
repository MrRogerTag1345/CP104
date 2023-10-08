"""
------------------------------------------------------------------------
t14.py
Converts minutes to days, hours, minutes.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-09-28"
------------------------------------------------------------------------
"""

# Defining Constants.
MIN_DAYS = 1440
HOUR = 60
DAY = 24

# Input from the user.
time = int(input("Enter number of minutes: "))

# Compute the math.
day = time // MIN_DAYS
remaining_day = time % MIN_DAYS
hours = remaining_day // HOUR
remaining_hours = hours % MIN_DAYS
mins = time % HOUR

# Prints the output and the answers. 
print("There are {} days, {} hours, and {} minutes in {} minutes".format(day, hours, mins, time))
