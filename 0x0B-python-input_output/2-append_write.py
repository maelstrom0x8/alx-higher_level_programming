#!/usr/bin/python3

"""A module for appending a string to the end of a text file (UTF-8).

This module provides a function, `append_write`, that appends a string
specified by `text` to the end of a text file specified by `filename`.
It returns the number of characters appended.
"""


def append_write(filename="", text=""):
    """Append a string to the end of a text file (UTF-8) and return the
        number of characters appended.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
