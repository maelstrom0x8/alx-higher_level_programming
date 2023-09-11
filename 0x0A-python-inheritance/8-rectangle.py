#!/usr/bin/python3

"""Rectangle class declaration"""

AbstractGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(AbstractGeometry):
    """Rectangle object"""
    def __init__(self, width, height):
        """Construct new instance of Rectangle"""
        self.integer_validator('width', width)
        self._width = width
        self.integer_validator('height', height)
        self._height = height
