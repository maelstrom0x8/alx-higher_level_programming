#!/usr/bin/python3

"""Abstract base class declaration for geometric objects"""

Base = __import__('6-base_geometry').BaseGeometry


class BaseGeometry:
    """Base definition for geometric objects"""

    def area(self):
        """Not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validation"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
