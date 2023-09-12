#!/usr/bin/python3

"""A module for loading a Python object from a JSON file.

This module provides a function, `load_from_json_file`, that takes a filename
as input and loads a Python object from a JSON file using the
`json.load` function.
"""

import json


def load_from_json_file(filename):
    """Load a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
