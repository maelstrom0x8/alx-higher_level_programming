#!/usr/bin/python3

"""A module for saving a Python object to a JSON file.

This module provides a function, `save_to_json_file`, that takes
a Python object and a filename as input and saves the object to a JSON
file using the `json.dump` function.
"""

import json


def save_to_json_file(my_obj, filename):
    """Save a Python object to a JSON file."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
