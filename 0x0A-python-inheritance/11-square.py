#!/usr/bin/python3

"""Square class declaration"""

AbstractRectangle = __import__('9-rectangle').Rectangle


class Square(AbstractRectangle):
    """This class models a square object"""
    def __init__(self, size):
        """Create a new square"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self._size = size

    def area(self):
        """Area of the Square object"""
        return self._size ** 2

    def __str__(self):
        """String representation for the square object"""
        return "[Square] {:d}/{:d}".format(self._width, self._height)
