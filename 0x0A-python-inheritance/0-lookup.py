#!/usr/bin/python3

"""A module for looking up the attributes and methods of an object.
This module defines a function, `lookup`, that takes an object as
input and returns a list of its attributes and methods."""


def lookup(obj: object):
    """Get a list of attributes and methods of an object."""

    return dir(obj)
