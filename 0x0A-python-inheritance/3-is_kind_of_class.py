#!/usr/bin/python3

"""A module for checking if an object is an instance of or derived from
a specific class. This module provides a function, `is_kind_of_class`, that
can be used to determine if an object is an instance of a specified class or
one of its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of or derived from
       a specific class."""
    if not isinstance(obj, a_class):
        return False
    return True
