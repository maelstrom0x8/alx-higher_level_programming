#!/usr/bin/python3

"""
This module defines a function 'print_square' to print a square pattern.

Functions:
    - print_square(size): Print a square pattern of a given size.
"""


def print_square(size):
    """
    Print a square pattern of a given size.

    Args:
        size (int): The size of the square to be printed.

    Raises:
        TypeError: If 'size' is not an integer.
        ValueError: If 'size' is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print("")
