"""
------------------------------------------------------------------------
functions.py
This is a function testing file.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-23"
------------------------------------------------------------------------
"""


# t01.py
def driver_license(ANS, var_one):
    """
    -------------------------------------------------------
    This function checks if the student answers are correct.
    use: c_answers, i_answers, list_answers = driver_license(ANS, var_one)
    -------------------------------------------------------
    Parameters:
        ANS - The answer to the test (list of str)
        var_one - The user input answer (str)
        
    Returns:
        c_answers - The correct answer (int > 0)
        i_answers - The incorrect answer (int > 0)
        list_answer - List of where the incorrect answer are (list of int)
    -------------------------------------------------------
    """
    
    # Defining Variables.
    c_answers = 0
    i_answers = 0
    list_answers = []
    
    # For loop runs until the last string in the list.
    for i in range(len(var_one)):
        # If check the if the user input is the correct answer.
        if var_one[i] == ANS[i]:
            c_answers += 1
        # Adds a counter to the incorrect inputs.
        else:
            list_answers.append(i)
            i_answers += 1
    
    # Return back to the main file.
    return c_answers, i_answers, list_answers


# t02.py
def sum_digit(my_str):
    """
    -------------------------------------------------------
    sums all the single digit numbers in my_str
    use: total = sum_digit(my_str)
    -------------------------------------------------------
    Parameters:
        my_str: string that has single-digit numbers (str)
        
    Returns:
        total: sum of all the single digit number (integer >= 0)
    -------------------------------------------------------
    """
    # Defining variables.
    total = 0
    
    # For loop runs until all the elements in the variable have been checked
    for i in range(len(my_str)):
        total = total + int(my_str[i])
     
    # Return back to the main file.    
    return total

        
# t03.py
def find_frequent(var_one):
    """
    -------------------------------------------------------
    This function gets finds most used character.
    use: result = find_frequent(var_one)
    -------------------------------------------------------
    Parameters:
        var_one - user input string value (str)
        
    Returns:
        return - most used character (str)
        
    -------------------------------------------------------
    """
    
    # Defining variables.
    list_char = []
    list_num = []
    
    # For loop runs until the last character of the string.
    for i in range(len(var_one)):
        # If checks the index at i and updates the most char counter in another list.
        if var_one[i] in list_char and var_one[i] != " ":
            list_num[list_char.index(var_one[i])] += 1
        
        else:
            list_char.append(var_one[i])
            list_num.append(1)
    
    # Finds which character is used the most.        
    result = list_char[list_num.index(max(list_num))]
      
    # Return back to the main file.    
    return result  
    
    
# t04.py
def add_spaces(my_str):
    """
    -------------------------------------------------------
    create a new string with added space between words
    use: new_str = add_spaces (my_str)
    -------------------------------------------------------
    Parameters:
        my_str: string that represents a sentence in which all the
                words are run together (no spaces), but the first
                character of each word is uppercase.
                my_str should has at least one character(str)
    
    Returns:
        new_str: new string in which the words are separated
                by spaces and only the first word starts with
                an uppercase character.
    -------------------------------------------------------
    """
    
    # Declaring variables.
    list = []
    temp = 0
    
    # For loop runs until the last char of the string.
    for i in range(len(my_str)):
        # If the ord is in the range then it will append everything before the capital letter.
        if ord(my_str[i]) >= 65 and ord(my_str[i]) <= 90:
            list.append(my_str [temp:i])
            temp = i 
    list.append(my_str[temp:])

    # This for run until all other words except the first world are lower case.
    for j in range(2, len(list)):
        var_x = list[j]
        list[j] = var_x.lower()

    # This joins the list into a string.
    new_str = " ".join(list[1:])
    
    # Return a string back to the main file.
    return new_str


def is_chain(var_one):
    """
    -------------------------------------------------------
    checks a list of strings to see if it has a word chain. Word before has the same last letter as the first letter of the next word.
    use: result = is_chain (list)
    -------------------------------------------------------
    Parameters:
        list: list of strings (list of str)
    
    Returns:
        result: True if there is a word chain, False if not(bool)
    -------------------------------------------------------
    """
    # Defining variables. 
    result = True
    
    # If checks if the words are a chain
    if(len(var_one) >= 2):
        for i in range(len(var_one) - 1):
            if var_one[i][-1] == var_one[i + 1][0]:
                result = True
            else:
                result = False
    else:
        result = False
    
    # Return back to the main file.    
    return result 
    
