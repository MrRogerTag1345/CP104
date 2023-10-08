"""
------------------------------------------------------------------------
functions.py
This is the functions testing program.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-10-25"
------------------------------------------------------------------------
"""


# t01.py
def pieces_produced(time, workers):
    """
    -------------------------------------------------------
    Calculates and returns the amount of pieces produced for
    a company.
    Use: result = pieces_produced(time_of_day, workers)
    -------------------------------------------------------
    Parameters:
        time - time (int > 0)
        workers - number of workers (int > 0)
    Returns:
        result - produced pieces (int)
    ------------------------------------------------------
    """
    # Constants.
    CON = 30
    CON2 = 40
    CON3 = 35
    
    # If statement for computing the results.
    if (time >= 6 and time <= 18): 
        
        # Checks to see where the data belongs and does the math.
        if ((time >= 6 and time <= 10) and (workers >= 1)):
            result = CON * workers
        
        elif ((time > 10 and time <= 14) and (workers >= 1)):
            result = CON2 * workers
    
        elif ((time > 14 and time <= 18) and (workers >= 1)):
            result = CON3 * workers
            
        else:
            result = -1

    else:
        result = -1
    
    # Return back to main file.
    return result


# t02.py
def num_day(num):
    """
    -------------------------------------------------------
    Converts a number to a day of the week.
    Use: days = num_day(number) 
    -------------------------------------------------------
    Parameters:
        num - number to day of the week (int >= 1)
    Returns:
        result - the day of the week (string)
    ------------------------------------------------------
    """
    
    # Constants.
    CON1 = 1
    CON2 = 2
    CON3 = 3
    CON4 = 4
    CON5 = 5
    CON6 = 6
    CON7 = 7
    
    # If statement that matches integer to day of the week.
    if num == CON1:
        result = "Monday"
    
    elif num == CON2:
        result = "Tuesday"
    
    elif num == CON3:
        result = "Wednesday"
        
    elif num == CON4: 
        result = "Thursday"
    
    elif num == CON5:
        result = "Friday"
        
    elif num == CON6:
        result = "Saturday"
        
    elif num == CON7:
        result = "Sunday"
    
    else:
        result = "Error"
    
    # Returns back to the main file.
    return result


# t03.py
def fed_tax(income):
    """
    -------------------------------------------------------
    Calculates the federal tax from the users income.
    Use: fed_return = fed_tax(income)
    -------------------------------------------------------
    Parameters:
        income - the users salary (int >= 1)
    Returns:
        math - the taxed amount of the users salary (float)
    ------------------------------------------------------
    """
    
    # Constants for taxes.
    TAX1 = 0.15
    TAX2 = 0.25
    TAX3 = 0.35
    
    # Constant for income.
    INCOME1 = 35000
    INCOME2 = 100000
    
    # If statements to calculate the federal tax.
    if (income <= INCOME1):
        math = income * TAX1
        
    elif (income > INCOME1) and (income <= INCOME2):
        math = ((INCOME1 * TAX1) + ((income - INCOME1) * TAX2))
    
    elif (income > INCOME2):
        math = ((INCOME1 * TAX1) + ((INCOME2 - INCOME1) * TAX2) + (income - INCOME2) * TAX3)

    # Return back to main file.
    return math

    
def prov_tax(income):
    """
    -------------------------------------------------------
    Calculates the provincial tax from the users income.
    Use: prov_return = prov_tax(income)
    -------------------------------------------------------
    Parameters:
        income - the users salary (int >= 1)
    Returns:
        math - the taxed amount of the users salary (float)
    ------------------------------------------------------
    """
    
    # Constant for taxes.
    TAX = 0.05
    INCOME = 50000
    
    # If statement to calculate provincial tax.
    if (income >= INCOME):
        math = (income - INCOME) * TAX
    else:
        math = 0
    
    # Return back to the main file. 
    return math
    

# t04.py
def pocket_colour(pocket):
    """
    -------------------------------------------------------
    Matches the pocket to a colour if it even or odd.
    Use: result = pocket_colour(number) 
    -------------------------------------------------------
    Parameters:
        pocket - a number that is either sorted to even or odd (int >= 0)
    Returns:
        result - the day of the week (string)
    ------------------------------------------------------
    """
    
    # If statement with nested if to check if values are even or odd.
    if pocket == 0:
        result = "green"
        
    elif (pocket >= 1 and pocket <= 10):
        if pocket in [1, 3, 5, 7, 9]:
            result = "red"
            
        else:
            result = "black"
            
    elif (pocket >= 11 and pocket <= 18):
        if pocket in [11, 13, 15, 17]:
            result = "black"
            
        else:
            result = "red"
            
    elif (pocket >= 19 and pocket <= 28):
        if pocket in [19, 21, 23, 25, 27]:
            result = "red"
        
        else:
            result = "black"
    elif (pocket >= 29 and pocket <= 36):
        if pocket in [29, 31, 33, 35]:
            result = "black"
            
        else:
            result = "black"
    else:
        result = "Error"
    
    # Return back to the main file.
    return result
            
        
# t05.py
def colour_mix(c_1, c_2):
    """
    -------------------------------------------------------
    Finds which primary colours mix with each other.
    Use: mix_colour = colour_mix(colour_one, colour_two)
    -------------------------------------------------------
    Parameters:
        c_1 - the fist colour input (string)
        c_2 - the second colour input (string)
    Returns:
        mix_colour - the two mixed colours result (string)
    ------------------------------------------------------
    """
    # Constants.
    RED = "red"
    BLUE = "blue"
    YELLOW = "yellow"
    
    # If statements.
    if c_1 == RED:
        # Check c_2 for which colour it belongs to.
        if (c_1 == RED and c_2 == BLUE) or (c_2 == RED and c_1 == BLUE):
            mix = "purple"
            
        elif (c_1 == RED and c_2 == YELLOW) or (c_2 == RED and c_1 == YELLOW):
            mix = "orange"
        
    elif (c_1 == BLUE and c_2 == YELLOW) or ((c_2 == BLUE and c_1 == YELLOW)):
        mix = "green"
        
    else:
        mix = "Error" 
        
    # Return back to main file.
    return mix
    
