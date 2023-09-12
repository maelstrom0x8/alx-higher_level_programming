#!/usr/bin/python3

"""A module defining a Student class with JSON serialization support.

This module defines a class, `Student`, which represents information about a
student, including their first name, last name, and age. The class provides a
method, `to_json`, for serializing a student object to a JSON-compatible
dictionary. The `to_json` method allows specifying a list of attributes to
include in the output.

Example:
    # Create a student object and serialize it to a JSON-compatible dictionary.
    student = Student("John", "Doe", 20)
    json_data = student.to_json()
    print(json_data)
    # Output: {'first_name': 'John', 'last_name': 'Doe', 'age': 20}

    # Serialize a student object including only specific attributes.
    attrs_to_include = ['first_name', 'age']
    json_data = student.to_json(attrs_to_include)
    print(json_data)  # Output: {'first_name': 'John', 'age': 20}
"""


class Student:
    """A class representing information about a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student object with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Serialize the student object to a JSON-compatible dictionary.

        Args:
            attrs (list, optional): A list of attribute names to include in
            the output. If provided, only the specified attributes will be
            included.

        Returns:
            dict: A dictionary containing the selected attributes and their
            values from the student object.
        """

        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
