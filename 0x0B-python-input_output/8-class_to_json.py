#!/usr/bin/python3

"""A module for converting a class object to a JSON-compatible dictionary.

This module provides a function, `class_to_json`, that takes a class object
as input and returns a dictionary containing its attributes and their
values, making it JSON-compatible.
"""


def class_to_json(obj):
    """Convert a class object to a JSON-compatible dictionary."""
    return obj.__dict__
