#!/usr/bin/python3
# 0-rectangle.py
# Amos Wachira
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):

        """Get values passed as args
            Args:
            width(int)
            height(int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of the rectangle"""
        return self__.width

    @width.setter
    def width(self, value):
        """Check if values are integers and set them to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
        @property
        def height(self):
            """Get the height of the rectangle"""
            return self.__height
        @height.setter
        def height(self, value):
            """Check if value is an int and not less than o
            Then set the value to height"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
