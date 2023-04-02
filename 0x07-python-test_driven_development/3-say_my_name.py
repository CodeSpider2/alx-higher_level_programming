#!/usr/bin/python3
#Amos Wachira

"""Print out my first and last names"""

def say_my_name(first_name, last_name=""):
    """Prints first and last names

    Args:
        first_name, last_name

    raises:
        TypeError if name is not a string

    """
    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
