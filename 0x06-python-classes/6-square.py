#!/usr/bin/python3


"""Square class declaration"""


class Square:
    """This class models a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int): The dimension of the square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the 'size' attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

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
        return self.__size**2

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value: tuple):
        """
        Get the current position of the square.

        Returns:
                tuple: A tuple representing the position of the square
                in the format (x, y).
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        x, y = value

        if not all(isinstance(num, int) for num in (x, y)) or not all(
            num >= 0 for num in (x, y)
        ):
            raise ValueError("position elements must be non-negative integers")

        self.__position = value

    def my_print(self):
        """Print in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
