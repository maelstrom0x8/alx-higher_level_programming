#!/usr/bin/python3

"""Rectangle class declaration"""

Base = __import__('7-base_geometry').BaseGeometry


class Rectangle(Base):
    """This class models a Rectangle"""
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self._width = width
        self.integer_validator('height', height)
        self._height = height

    def area(self):
        """The area of the Rectangle"""
        return self._width * self._height

    def __str__(self):
        """String representation for the rectangle object"""
        return "[Rectangle] {:d}/{:d}".format(self._width, self._height)
