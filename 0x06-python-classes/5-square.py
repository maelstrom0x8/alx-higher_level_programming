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
        self.size = size

    @property
    def size(self):
        """
        Getter method for the 'size' attribute.

        Returns:
            int: The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter method for the 'size' attribute.

        Args:
            value (int): The new size to set.

        Raises:
            ValueError: If 'value' is not a positive integer.
            TypeError: If 'value' is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """Print in stdout the square with the character #"""
        for _ in range(self.__size):
            print("#" * self.__size)

        if self.__size == 0:
            print("")
