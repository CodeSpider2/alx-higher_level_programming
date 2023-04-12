#!/usr/bin/python3
#Amos Wachira
"""A function that returns an object represented by a json string"""

def from_json_string(my_str):
    """
        Args:
            my_str:The object to be returned as a json
        Returns:
            A json object of the argument

    """
    import json
    return json.loads(my_str)
