"""
------------------------------------------------------------------------
functions.py
Functions testing program.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-08"
------------------------------------------------------------------------
"""


# t01.py
def perfect_square(square):
    """
    -------------------------------------------------------
    Calculates all number with a perfect square up to the 
    inputed number.
    a company.
    Use: result = perfect_square(square))
    -------------------------------------------------------
    Parameters:
        square - input number by the user (int > 0)
        
    Returns:
        var_one - numbers that are perfect square up to
        the number (int)
    ------------------------------------------------------
    """
    # Defining variables.
    var_one = ""
    
    # If statement that checks if number is not negative.
    if (square < 0):
        var_one = "Error: you entered a negative number"
    
    # For loop that finds values of perfect square. 
    for i in range(1, square + 1):
        # If statement for finding if the loop run number = to a perfect square.
        if (i ** 2 <= square):
            var_one += str(i ** 2) + " "
        else:
            break  
        
    # Return result.             
    return var_one


# t02.py
def factorial(num):
    """
    -------------------------------------------------------
    Calculates the factorial of the number inputed.
    a company.
    Use: result = factorial(var_one)
    -------------------------------------------------------
    Parameters:
        num - input number by the user (int > 0)
        
    Returns:
        result - the result of the factorial of the number
        inputed (int)
    ------------------------------------------------------
    """
    # Defining variables.
    result = 1

    # For loop that runs to calculate all the numbers that are a factorial.
    for i in range(1, num + 1):
        result *= i 

    # Return result.        
    return result

        
# t03.py
def is_prime(num):
    """
    -------------------------------------------------------
    Calculates if the input number is a prime number or not.
    a company.
    Use: result = perfect_square(square))
    -------------------------------------------------------
    Parameters:
        num - input number by the user (int > 0)
        
    Returns:
        result - either it is a prime number or not (boll)
    ------------------------------------------------------
    """
    # Defining variables.
    result = True
    
    # For loop runs from 2 till the end of the num -1.
    for i in range(2, num):
        # If compares if there is a remainder of zero.
        if (num % i == 0):
            result = False 
    
    # Return result.    
    return result

    
# t04.py
def print_pattern(num_rows):
    """
    -------------------------------------------------------
    This function draws a character but each line adds a space
    from the first character to the last.
    Use: result = print_pattern(var_one)
    -------------------------------------------------------
    Parameters:
        num_rows - input number by the user (int > 0)
        
    Returns:
        return - nothing
    ------------------------------------------------------
    """
    # Defining variables.
    result = ""
    
    # For loop adds the spacing.
    for i in range(num_rows):
        print("#" + result + "#")
        result += " "

    # Return result. 
    return

   
# t05.py
def winner():
    """
    -------------------------------------------------------
    This function determines which team is going to win from
    the amount of times the color entered wins.
    Use: red, green = winner()
    -------------------------------------------------------
    Preconditions:
        var_one - the color of a team (string)
        
    Returns:
        red - the number of times red wins (int > 0)
        green - the number of times green wins (int > 0)
    ------------------------------------------------------
    """
    
    # Defining variables.
    red = 0
    green = 0
    
    # For loop that runs 100 times until broken.
    for i in range(100):
        var_one = (input("Enter the winning team: "))
        # if determines if the series has ended or not.
        if (var_one == ""):
            break
        else:
            # Checks if which color has won.
            if (var_one == "red") or (var_one == "RED"):
                red += 1
            elif (var_one == "green") or (var_one == "GREEN"):
                green += 1
    
    # Return Statement.
    return red, green
