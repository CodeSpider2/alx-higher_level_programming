#!/usr/bin/python3
#Amos Wachira

"""Define a function to print a square"""

def print_square(size):
    """Print a square based on size argument

    Args:
        size(int):Size of the square

    raises:
        TypeError:If size is not int
        ValueError:If size is less than zero
    """
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
