"""
------------------------------------------------------------------------
functions.py

------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-02"
------------------------------------------------------------------------
"""
from random import randint
import string


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    count = 1
    
    number = randint(1, high)
    guess = int(input("Guess: "))
    
    while guess != number:
        if guess > number:
            print ("Too high, try again.")
            count += 1
        
        elif (guess < number):
            print("Too low, try again.")
            count += 1
            
        guess = int(input("Guess: "))
    
    print("Congratulations - good guess!")
    
    return count


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    RATE = rate / 100
    
    years = 0
    final = current
    
    while (final < target): 
        final = final + (final * RATE)
        years += 1
    return(years)


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    
    value = float(input("First value: "))  
    minimum = value
    maximum = value
    total = value 
    count = 1
    value = float(input("Next positive value:"))
    while(value >= 0):
        count += 1
        total = total + value
        if (value < minimum):
            minimum = value
        elif (value > maximum):
            maximum = value
        value = float(input("Next positive value:"))
    average = total / count
    return(minimum, maximum, total, average)

   
def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    
    day = 1
    new_day = "Y"
    result = 0
    r1 = 0
    r2 = 0
    r3 = 0

    while new_day != "N":
        print("Day ", day)
        print()
        
        v1 = float(input("How much was breakfast? $"))
        v2 = float(input("How much was lunch? $"))
        v3 = float(input("How much was supper? $"))
        total = (v1 + v2 + v3)
        print("Your total for the day was $", total)
        
        r1 = r1 + v1
        r2 = r2 + v2
        r3 = r3 + v3
        result = result + total
        new_day = (input("Were you away another day (Y/N)? "))
        day += 1  
    
    print("Total:")
    print("Breakfast:   $ {:.2f}".format(r1))
    print("Lunch:       $ {:.2f}".format(r2))
    print("Supper:      $ {:.2f}".format(r3))
    print("Grand Total: $ {:.2f}".format(result))
    
    return
   
