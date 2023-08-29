#!/usr/bin/python3

"""Square class declaration"""


class Square:
    """This class models a Square"""

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The dimension of the square.
        """
        self.__size = size
