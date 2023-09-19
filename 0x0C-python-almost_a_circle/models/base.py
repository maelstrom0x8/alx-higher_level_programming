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

import csv
import json
import turtle


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
        filename = ''.join([cls.__name__, '.json'])
        with open(file=filename, encoding='utf-8', mode='w') as file:
            if list_objs is None or not isinstance(list_objs, list):
                file.write("[]")
            else:
                res = [x.to_dictionary() for x in list_objs]
                file.write(Base.to_json_string(res))

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
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of instances to a CSV file.

        Args:
            cls: The class.
            list_objs (list): A list of instances to serialize.

        Returns:
            None
        """
        filename = ''.join([cls.__name__, ".csv"])
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes instances from a CSV file.

        Args:
            cls: The class.

        Returns:
            list: A list of instances.
        """
        filename = ''.join([cls.__name__ + ".csv"])
        try:
            with open(filename, "r", newline="") as fil:
                if cls.__name__ == "Rectangle":
                    fields = cls.__name__ == "Rectangle" and ["id", "width",
                                                              "height", "x",
                                                              "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(fil, fieldnames=fields)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws instances of rectangles and squares
        on a Turtle graphics screen.

        Args:
            list_rectangles (list): A list of Rectangle instances to draw.
            list_squares (list): A list of Square instances to draw.

        Returns:
            None
        """
        g_obj = turtle.Turtle()
        g_obj.screen.bgcolor("#EBEBEB")
        g_obj.pensize(2)
        g_obj.shape("triangle")

        g_obj.color("#414141")
        for rect in list_rectangles:
            g_obj.showturtle()
            g_obj.up()
            g_obj.goto(rect.x, rect.y)
            g_obj.down()
            for i in range(2):
                g_obj.forward(rect.width)
                g_obj.left(90)
                g_obj.forward(rect.height)
                g_obj.left(90)
            g_obj.hideturtle()

        g_obj.color("#212121")
        for sq in list_squares:
            g_obj.showturtle()
            g_obj.up()
            g_obj.goto(sq.x, sq.y)
            g_obj.down()
            for i in range(2):
                g_obj.forward(sq.width)
                g_obj.left(90)
                g_obj.forward(sq.height)
                g_obj.left(90)
            g_obj.hideturtle()

        turtle.exitonclick()
