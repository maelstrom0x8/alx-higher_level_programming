#!/usr/bin/python3

"""A module for converting a JSON-formatted string to a Python object.

This module provides a function, `from_json_string`, that takes a
JSON-formatted string as input and returns a Python object representation
of that string using the `json.loads` function.
"""

import json


def from_json_string(my_str):
    """Convert a JSON-formatted string to a Python object."""
    return json.loads(my_str)
