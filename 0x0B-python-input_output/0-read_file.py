#!/usr/bin/python3

"""A module for reading and printing the contents of a text file (UTF-8).
This module provides a function, `read_file`, that reads the contents of a
text file specified by `filename` and prints each line to standard output.
"""


def read_file(filename=''):
    """Read and print the contents of a text file (UTF-8)."""

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
