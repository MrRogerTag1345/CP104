"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-16"
------------------------------------------------------------------------
"""


def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """

    hydroxide = chemical.endswith("OH")

    return hydroxide


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    
    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:13]

    return pc, pi, pq


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        None
    -------------------------------------------------------
    """
    if(product_code[0:3].isalpha() and product_code[0:3].isupper() and len(product_code[0:3]) == 3):
        print("Category {} is valid.".format(product_code[0:3]))
    else:
        print("Category {} is not valid.".format(product_code[0:3]))
        
    if(product_code[3:7].isdigit() and len(product_code[3:7]) == 4):
        print("ID {} is valid.".format(product_code[3:7]))
        
    else:
        print("ID {} is not valid.".format(product_code[3:7]))
    
    if(product_code[7:8].isupper() and len(product_code[7:]) > 0):
        print("Qualifier {} is valid.".format(product_code[7:]))
        
    else:
        print("Qualifier {} is not valid.".format(product_code[7:]))
    return
    

def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    
    count = 0
    
    for i in s:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            count += 1
    
    return count

    
def calculate(expr):
    """
    -----------------------------------------------------------------
    Treats expr as a math expression and evaluates it.
    expr must have the following format:
        operand1 operator operand2
    operators are: +, -, *, /, %
    operands are one-digit integer numbers
    Return None if second operand is zero for division.
    Use: result = calculate(expr)
    -----------------------------------------------------------------
    Parameters:
        expr - an arithmetic expression to be calculated (str)
    Returns:
        result - The result of arithmetic expression (float)
    -----------------------------------------------------------------
    """
    x = int(expr[0])
    opp = expr[2]
    y = int(expr[4])
    
    if opp == "+":
        result = x + y
    elif opp == "/":
        if y == 0:
            result = None
        else:
            result = x / y
    elif opp == "-":
        result = x - y
    elif opp == "*":
        result = x * y
    elif opp == "%":
        if y == 0:
            result = None
        else:
            result = x % y
        
    return result    
    
