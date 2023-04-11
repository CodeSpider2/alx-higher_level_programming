#!/usr/bin/python3
#Amos Wachira
"""Define an class Mylist which inherits from the base class list"""

class MyList(list):
    """Sorts a list using the inbiult method and prints it out"""

    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        print(sorted(self))
