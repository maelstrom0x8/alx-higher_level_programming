#!/usr/bin/python3

"""A module for checking if an object inherits from a specific class.
This module provides a function, `inherits_from`, that can be used to determine
if an object is an instance of a subclass of a specified class.
"""


def inherits_from(obj, a_class):
    """Check if an object inherits from a specific class."""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
