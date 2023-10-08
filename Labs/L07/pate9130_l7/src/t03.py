"""
------------------------------------------------------------------------
t03.py
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-02"
------------------------------------------------------------------------
"""

from functions import population_growth

t1 = int(input("Target population: "))
c1 = int(input("Current population: "))
rate = int(input("Growth rate (%): "))

result = population_growth(t1, c1, rate)

print("Years to reach target:", result)

