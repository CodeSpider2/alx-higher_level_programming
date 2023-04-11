#!/usr/bin/python3

"""
This module defines a function that checks only sub class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.
    Args:
        obj (object): Object to check.
        a_class (class): Specified class.
    Returns:
        if obj is a subclass of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return Falsei
