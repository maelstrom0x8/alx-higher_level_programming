#!/usr/bin/python3

"""A module for writing a string to a text file (UTF-8) and returning
the number of characters written.

This module provides a function, `write_file`, that writes a string
specified by `text` to a text file specified by `filename`. It returns
the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8) and return
       the number of characters written."""

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
