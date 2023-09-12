#!/usr/bin/python3

"""A module for converting a Python object to a JSON-formatted string.

This module provides a function, `to_json_string`, that takes a Python
object as input and returns a JSON-formatted string representation of
that object using the `json.dumps` function.
"""

import json


def to_json_string(my_obj):
    """Convert a Python object to a JSON-formatted string."""
    return json.dumps(my_obj)
