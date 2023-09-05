#!/usr/bin/python3

"""
Module: add_integer

This module defines a function 'add_integer' that adds two numbers and returns
their sum as an integer. Float inputs are rounded down to integers.

Functions:
    - add_integer(a, b=98): Add two numbers and return the sum as an integer.

Usage:
    - Import the module and use the 'add_integer' function with two
    numeric arguments.

Examples:
    >>> import add_integer
    >>> add_integer(3, 5)
    8
    >>> add_integer(3.5, 2.5)
    5

Exceptions:
    - TypeError: Raised when 'a' or 'b' is not a number.

Note:
    - 'add_integer' can handle integer and float inputs,
    rounding floats down to integers.
"""


def add_integer(a, b=98):
    """Return the sum of a and b.

    Float arguments are casted to ints before calculating the sum.

    Raises:
        TypeError: If a or b is a not an int or float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    sum = int(a) + int(b)
    return sum
