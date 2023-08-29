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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size ** 2)
