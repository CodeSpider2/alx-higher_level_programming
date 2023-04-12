#!/usr/bin/python3
#Amos Wachira
"""Define a function to load from a json"""

def load_from_json_file(filename):
    """
    Args:
        filename:The file where json will be loaded from
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
