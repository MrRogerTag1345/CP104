"""
------------------------------------------------------------------------
This programe conver seconds into days, hours, minutes, seconds
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-09-21"
------------------------------------------------------------------------
"""

# Defining the constants.
time = int(input("Number of seconds: "))
MIN = 60
HOUR = MIN * 60
DAY = HOUR * 24

# Computes the math.
day = time // DAY
mod_days = time % DAY
hour = mod_days // HOUR
mins = ((mod_days)) % HOUR // MIN
sec = ((mod_days % HOUR) % MIN)

# Prints the output and the answers. 
print("Day:", day, "Hours:", hour, "Minutes:", mins, "Seconds:", sec)
