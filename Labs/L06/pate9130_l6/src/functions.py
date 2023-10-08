"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-10-26"
------------------------------------------------------------------------
"""


def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """
    
    total = 0
    
    for i in range(2, num + 1, 2):
        total = total + i
    
    # Return
    return total


def draw_rectangle(height, width, char):
    """
    -------------------------------------------------------
    Prints a rectangle of height and width characters using
    the char character.
    Use: draw_rectangle(height, width, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """

    print()
    
    for i in range(height):
        print (char * width)
        
    # Return.
    return


def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for i in range(n, 1, -1):
        print(n, "bottles of beer on the wall,", n , "bottles of beer.")
        print("Take one down, pass it around,", n - 1, "bottles of beer on the wall.")
        n = n - 1
        
    return


def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    
    print("Age         Salary")
    print("------------------")
    
    for i in range(age, 66, 1):
        print("{:<9d} {:,.2f}".format(i, salary))
        salary = salary / 100 * increase + salary
    return


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    -------------------------------------------------------
    """
    
    total_n = 0
    last_value = 0
    value_1 = float(input("First value: "))
    for i in range(1, n):
        value_2 = float(input("Next value: "))
        if(last_value > value_2 and value_2 < value_1):
            minimum = value_2
        elif(last_value < value_2 and value_2 > value_1):
            maximum = value_2
        else:
            minimum = value_1
            maximum = value_1

        last_value = value_2
        total_n = total_n + value_2

    total = total_n + value_1
    average = total / n

    return(minimum, maximum, total, average)
    
