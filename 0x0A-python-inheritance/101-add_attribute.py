#!/usr/bin/python3

"""Attribute Manipulation

This module provides a function, `add_attribute`, that allows
you to add a new attribute to an object dynamically, as long as
the object has a `__dict__` attribute. It raises a `TypeError` if the
object does not support attribute addition.
"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object dynamically.

    Args:
        obj (object): The object to which the attribute will be added.
        att (str): The name of the new attribute.
        value (any): The value to assign to the new attribute.

    Raises:
        TypeError: If the object does not support dynamic attribute addition
        (i.e., does not have a `__dict__` attribute).
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
