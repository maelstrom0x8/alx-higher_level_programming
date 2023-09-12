#!/usr/bin/python3

"""A module defining a Student class and its JSON serialization method.

This module defines a class, `Student`, which represents information
about a student, including their first name, last name, and age. The class
also provides a method, `to_json`, for serializing a student object to
a JSON-compatible dictionary."""


class Student:
    """A class representing information about a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student object with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Serialize the student object to a JSON-compatible dictionary."""
        return self.__dict__
