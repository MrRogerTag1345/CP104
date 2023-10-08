"""
------------------------------------------------------------------------
functions.py
This is a functions testing program.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-15"
------------------------------------------------------------------------
"""


# t01.py
def read_positive():
    """
    -------------------------------------------------------
    Input a positive number into a list and returns list.
    Use: list = read_positive()
    -------------------------------------------------------
    Preconditions:
        var_one - positive user input (int > 0)
    Returns:
        list  - positive number (list of ints > 0)
    -------------------------------------------------------
    """
    # Constants.
    ZERO = 0
    
    # Declaring list.
    list = []
    
    # User input.
    var_one = int(input("Enter a positive number: "))
    
    # While loop 
    while var_one != ZERO:
        # If statement determines if the variable input is greater than zero.
        if (var_one > 0):
            # Adds the positive integer to the list and asks the user for the input again.
            list.append(var_one)
            var_one = int(input("Enter a positive number: "))
        else:
            # If the integer is negative then ask the user to input another integer.
            var_one = int(input("Enter a positive number: "))
    
    # Return back to the main file.
    return list


# t02.py
def find_target(list, target):
    """
    -------------------------------------------------------
    This function finds the target value in the provided list.
    Use: arr = find_target(list, var_one)
    -------------------------------------------------------
    Parameter:
        list - list of positive numbers (list of int > 0)
        target - value of integer that is a key to find the locations of the
        values in the list (int > 0)
    Returns:
        arr  - location of the number in the list (list of ints > 0)
    -------------------------------------------------------
    """
    # Declaring a list.
    arr = []
    
    # This for loop runs until the last variable in the list.
    for i in range(len(list)):
        # If checks if the number is in the target.
        if list[i] == target:
            arr.append(i)
    
    # Return back to main file.
    return arr


# t03.py
def largest_odd(list):
    """
    -------------------------------------------------------
    This function finds the target odd value in the list.
    Use: odd = largest_odd(list)
    -------------------------------------------------------
    Parameter:
        list - list of positive numbers (list of int > 0)
    Returns:
        temp  - the value of the largest odd integer (int > 0)
    -------------------------------------------------------
    """
    # Declaring a list.
    temp = -1
    
    # Runs loop until the last variable in the list.
    for i in range(len(list)):
        # If checks is the number in the list % 2 is either 0 or 1.
        if (list[i] % 2) == 1:
            if (list[i] > temp):
                temp = list[i] 
    
    # Return back to main file.
    return temp


# t04.py   
def reverse_list(list):
    """
    -------------------------------------------------------
    This function reverses the list.
    Use: arr = reverse_list(list)
    -------------------------------------------------------
    Parameter:
        list - list of positive numbers (list of int > 0)
    Returns:
        arr  - reverse of the positive list (list of int > 0)
    -------------------------------------------------------
    """
    
    # Declaring a list.
    arr = []
    
    # Runs loop unitl the last character, however its starting at the end and moving to the start.
    for i in range(len(list) - 1, -1, -1):
        arr.append(list[i])
    
    # Return back to main file.    
    return arr
          
