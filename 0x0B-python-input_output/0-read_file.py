#!/usr/bin/python3
#Amos Wachira
"""Define a function that reads a text file without handling exceptions"""

def read_file(filename=""):
    """
    Args:
        filename:The name of the file to be read
    Prints out the lines of the file
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
