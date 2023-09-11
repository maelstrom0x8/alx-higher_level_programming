#!/usr/bin/python3

"""A module for checking if an object belongs to a specific class.
This module provides a function, `is_same_class`, that can be used
to determine if an object is an instance of a specified class."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a specific class."""
    if type(obj) is not a_class:
        return False
    return True
