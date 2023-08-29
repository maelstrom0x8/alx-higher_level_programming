#!/usr/bin/python3

"""Square class declaration"""


class Square:
    """This class models a Square"""

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The dimension of the square.
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
