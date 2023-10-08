"""
------------------------------------------------------------------------
functions.py
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2020-11-23"
------------------------------------------------------------------------
"""


def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    
    list = []
    i = 0
    line = fh.readline()
    
    while line != "" and i < n:
        i += 1
        line = fh.readline()
     
    if line != "":
        list = line.strip().split(",")
    
    return list


def customer_append(fh, fields):
    """
    -------------------------------------------------------
    Appends a customer record to a comma-delimited sequential file.
    Use: customer_append(fh, fields)
    -------------------------------------------------------
    Parameters:
        fh - file to add to (file handle - already open for appending)
        fields - a list of the field data to append to the file (list)
    Returns:
       None
    -------------------------------------------------------
    """
    
    n = len(fields)
    
    for i in range(n - 1):
        fh.write("{},".format(fields[i]))
    fh.write("{}\n".format(fields[n - 1]))
    return


def number_stats(fh):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """
    total = 0
    count = 0

    largest = 1 
    smallest = 1

    for line in fh:
        mark = int(line)
        if(largest < mark):
            largest = mark
        elif(smallest > mark):
            smallest = mark
        total = total + mark
        count = count + 1

    average = total / count
    return smallest, largest, total, average

        
def count_frequency_value(fh, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fh.
    Use: count = count_frequency_value(fh, value)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fh (int)
    ------------------------------------------------------
    """
    
    count = 0
    nums = []
    
    for line in fh:
        nums.append(int(line.strip()))
                    
    for j in range(len(nums)):
        if nums[j] == value:
            count += 1
    return count


def file_copy(fh_1, fh_2):
    """
    -------------------------------------------------------
    Copies the contents of fh_1 to fh_2.
    Any contents of fh_2 are overwritten.
    Use: file_copy(fh_1, fh_2)
    -------------------------------------------------------
    Parameters:
        fh_1 - source file (file handle - already open for reading)
        fh_2 - target file (file handle - already open for writing)
    Returns:
        None
    ------------------------------------------------------
    """     
    i = 0 
    records = ""
    
    line = fh_1.readline()
    
    while line != "":
        records += line
        line = fh_1.readline()
        i += 1
    fh_2.write(records)
    return  
    
