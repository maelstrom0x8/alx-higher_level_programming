#!/usr/bin/python3

"""Rectangle class declaration"""


class Rectangle:
    """Models a rectangle object"""

    def __init__(self, width=0, height=0):
        """Rectangle constructor

        Args:
            width (int): The width.
            height (int): The height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle"""
        return self.width

    @property
    def height(self):
        """Set the rectangle height"""
        return self.height

    @width.setter
    def width(self, value):
        """Set the rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @height.setter
    def height(self, value):
        """Get the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value
