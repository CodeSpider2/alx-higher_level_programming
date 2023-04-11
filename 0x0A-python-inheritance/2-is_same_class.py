#!/usr/bin/python3
#Amos Wachira
"""Define a class to check an instance"""

def is_same_class(obj, a_class):
    """Checks if the obj argument is of the same instance as a certain class

    Args:
        obj:The object to check
        a_class:The class to match the type obj to
    Returns:
        True if the obj is same instance else returns False
        """
        if type(obj) == a_class:
            return True
        return False
