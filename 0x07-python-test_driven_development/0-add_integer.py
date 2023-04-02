#!/usr/bin/python3

""" Function to add two integers  """

def add_integer(a, b=98):
    """
    The funtion checks if the inputs are integers or floats
    and raises an error if they are not.
    The inputs are then converted to integers and the function 
    returns the sum.
    
    """
    if a not in [int, float]:
        raise TypeError("a must be an integer")
    if b not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a+b)
