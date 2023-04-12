#!/usr/bin/python3
#Amos Wachira
"""Module containing a function that returns JSON representation of an object"""

def to_json_string(my_obj):
    """
    Args:
        my_obj:The object to be returned as a json
    Return:
        A json representation.
    """
    import json
    return(json.dumps(my_obj))
