#!/usr/bin/python3
#0-lookup.py
#Amos Wachira
"""Object lookup function definition"""


def lookup(obj):
    """Returns a list of available attributes in an object"""
    return (dir(obj))
