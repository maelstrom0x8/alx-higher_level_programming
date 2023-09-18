#!/usr/bin/python3

"""square.py

This module defines the Square class, a subclass of the Rectangle class,
representing squares with various properties.

Classes:
    Square: A class representing squares.

Attributes:
    None

Methods:
    __init__(self, size, x=0, y=0, id=None): Initializes a Square instance
    with specified attributes.
    size(self): Getter method for the size attribute.
    size(self, value): Setter method for the size attribute.
    update(self, *args, **kwargs): Updates the attributes of the square.
    to_dictionary(self): Returns a dictionary representation of the square.
    __str__(self): Returns a string representation of the square.

"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing squares.

    Attributes:
        id (int): The identifier for the square.
        __width (int): The width of the square.
        __height (int): The height of the square (same as width for squares).
        __x (int): The x-coordinate of the square.
        __y (int): The y-coordinate of the square.

    Methods:
        __init__(self, size, x=0, y=0, id=None): Initializes a Square instance
        with specified attributes.
        size(self): Getter method for the size attribute.
        size(self, value): Setter method for the size attribute.
        update(self, *args, **kwargs): Updates the attributes of the square.
        to_dictionary(self): Returns a dictionary representation of the square.
        __str__(self): Returns a string representation of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance with specified attributes.

        Args:
            size (int): The size (width and height) of the square.
            x (int, optional): The x-coordinate of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the square. Defaults to 0.
            id (int, optional): The identifier for the square. Defaults to
            None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size attribute.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the square.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.

        Notes:
            The method can be used with positional arguments (args) or keyword
            arguments (kwargs).
            When using positional arguments, the following order should be
            followed:
                1. id
                2. size
                3. x
                4. y
            If an attribute is not provided, its value remains unchanged.

        Example:
            To update the size and x-coordinate:
                square.update(10, x=5)
            To update the y-coordinate using keyword argument:
                square.update(y=3)

        """
        attribute_names = ['id', 'size', 'x', 'y']
        keys = list(kwargs.keys())
        if args and len(args) != 0:
            for i, value in enumerate(args):
                i < len(attribute_names) and setattr(self, attribute_names[i],
                                                     value)
        elif kwargs and len(kwargs) != 0:
            for k in keys[:len(keys)]:
                if k == 'id':
                    if kwargs.get('id') is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = kwargs.get('id', self.id)
                    continue
                if not isinstance(kwargs.get(k), int):
                    if k in 'size':
                        raise TypeError('width must be an integer')
                    raise TypeError(k + ' must be an integer')
                if k in 'size' and kwargs[k] <= 0:
                    raise ValueError('width must be > 0')
                if kwargs[k] < 0:
                    raise ValueError(k + ' must be >= 0')

            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """Returns a dictionary representation of the square.

        Returns:
            dict: A dictionary representing the attributes of the square.
        """
        return {
            "id": self.id, "x": self.x, "size": self.size,
            "y": self.y
        }

    def __str__(self):
        """Returns a string representation of the square.

        Returns:
            str: A string representing the square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
