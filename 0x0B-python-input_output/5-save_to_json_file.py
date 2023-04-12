#!/usr/bin/python3
#Amos Wachira
"""Define a function in this module to save a text file as json"""

def save_to_json_file(my_obj, filename):
    """
    Args: 
        my_obj:Saves my this object to the filename argument as json
        filename:The file to be saved to
    Returns:
            void
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
