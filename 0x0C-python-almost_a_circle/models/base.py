#!/usr/bin/python3
"""base.py

This module contains the Base class and related utility methods for
serializing and deserializing objects to JSON.

Classes:
    Base: The base class for serializable objects.

Functions:
    to_json_string(list_dictionaries): Serialize a list of dictionaries to a
    JSON-formatted string.
    save_to_file(list_objs): Save a list of objects to a JSON file.
    from_json_string(json_string): Deserialize a JSON-formatted string to a
    list of dictionaries.
    create(**dictionary): Create an object instance with attributes based on a
    dictionary.
    load_from_file(): Load objects from a JSON file and return a list of
    instances.
"""

import json


class Base:
    """Base class for serializable objects.

    Attributes:
        id (int): The identifier for the object.

    Class Attributes:
        __nb_objects (int): A counter to track the number of objects created.

    Methods:
        to_json_string(list_dictionaries): Serialize a list of dictionaries to
        a JSON-formatted string.
        save_to_file(list_objs): Save a list of objects to a JSON file.
        from_json_string(json_string): Deserialize a JSON-formatted string t
        a list of dictionaries.
        create(**dictionary): Create an object instance with attributes based
        on a dictionary.
        load_from_file(): Load objects from a JSON file and return a list of
        instances.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base object with an optional identifier.

        Args:
            id (int, optional): The identifier for the object. Defaults to
            None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serialize a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list of dict): The list of dictionaries to
            serialize.

        Returns:
            str: A JSON-formatted string representing the serialized data.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects to be serialized and saved to
            a JSON file.
        """
        if list_objs is None or not isinstance(list_objs, list):
            res = None
        else:
            res = [x.to_dictionary() for x in list_objs]
        json_str = Base.to_json_string(res) if isinstance(res, list) else "[]"
        filename = ''.join([cls.__name__, '.json'])
        with open(file=filename, encoding='utf-8', mode='w') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string: str):
        """Deserialize a JSON-formatted string to a list of dictionaries.

        Args:
            json_string (str): The JSON-formatted string to be deserialized.

        Returns:
            list: A list of dictionaries representing the deserialized data.
        """
        return [] if not json_string else json.loads(json_string)
        # out = json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an object instance with attributes based on a dictionary.

        Args:
            **dictionary: Keyword arguments representing object attributes.

        Returns:
            Base: An instance of the class with attributes set based on the
            provided dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load objects from a JSON file and return a list of instances.

        Returns:
            list: A list of instances loaded from the JSON file.
        """
        filename = cls.__name__ + '.json'
        instances = []

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                json_str = file.read()
                data = json.loads(json_str)
                for item in data:
                    instances.append(cls.create(**item))
        except FileNotFoundError:
            pass

        return instances
