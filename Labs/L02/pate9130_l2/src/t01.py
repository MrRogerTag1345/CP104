"""
------------------------------------------------------------------------
This program will convert celsius temperature to fahrenheit.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-09-21"
------------------------------------------------------------------------
"""

# Get the temperature input in degrees.
F = 32
c = int(input("Temperature (C):"))

# The math process to convert from Celsius to Fahrenheit.
ans = 9 / 5 * c + F

# Print Statements.
print("Temperature (C):", c)
print("Temperature (F):", ans)
