#!/usr/bin/python3

"""Custom Integer Class

This module defines a custom integer class, `MyInt`, that inherits
from the built-in `int` class. `MyInt` overrides the equality and
inequality comparison methods to have opposite behavior compared to
the standard `int` class.

Classes:
    MyInt: A custom integer class with modified equality and
    inequality comparison behavior.
"""


class MyInt(int):
    """A custom integer class with overridden equality and
       inequality operators.

    The `MyInt` class provides custom behavior for the equality
    (`==`) and inequality (`!=`) operators. It considers
    two integers equal when their numeric values are not equal.

    """

    def __eq__(self, __value: object):
        """Override the equality operator.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if the numeric values of the two objects are
            not equal, False otherwise.
        """
        return self.real != __value

    def __ne__(self, __value: object):
        """Override the inequality operator.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if the numeric values of the two objects
            are equal, False otherwise.
        """
        return self.real == __value
