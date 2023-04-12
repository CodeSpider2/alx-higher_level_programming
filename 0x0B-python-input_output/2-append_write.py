#!/usr/bin/python3
#Amos Wachira
"""
    Module 4-append_write
    Function to append a text in a certain file
"""

def append_write(filename="", text=""):
    """
    Args:
        filename:The name of the file to append the text.
        text:the text to be appended to the file

    Returns:
        number of characters added.
    """
    
    with open(filename, mode="a", encoding="utf-8") as file:
        return(file.write(text))
