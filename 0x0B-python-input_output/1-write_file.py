#!/usr/bin/python3
#Amos Wachira
"""Define a function to write a file"""

def write_file(filename="", text=""):
    """
    Args:
        filename:The name of the file to be written.
        text:The name of the text to write in the file.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return(file.write(text))
