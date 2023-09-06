#!/usr/bin/python3

"""
This module defines a function 'text_indentation' to
format and print text with proper indentation.

Functions:
    - text_indentation(text): Format and print text with proper indentation.
"""


def text_indentation(text):
    """
    Format and print text with proper indentation.

    Args:
        text (str): The text to be formatted and printed.

    Raises:
        TypeError: If 'text' is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    end = 0
    px = -1

    while end != len(text):
        for k in text[start:]:
            if k in ".:?":
                print(text[start:end + 1].strip(), end="\n\n")
                start = end + 1
                px = end
            end += 1
    print(text[px + 1: len(text)].strip(), end='')
