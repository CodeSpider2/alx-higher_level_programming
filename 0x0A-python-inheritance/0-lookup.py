#!/usr/bin/python3
#Amos Wachira
"""Object lookup function definition"""

def lookup(obj):
    """Returns a list of available attributes in an object"""
    return(dir(obj))
