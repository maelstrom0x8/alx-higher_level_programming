#!/usr/bin/python3

"""Abstract base class declaration for geometric objects"""

Base = __import__('5-base_geometry').BaseGeometry


class BaseGeometry(Base):
    """Base definition for geometric objects"""
    def area(self):
        """Not yet implemented"""
        raise Exception('area() is not implemented')
