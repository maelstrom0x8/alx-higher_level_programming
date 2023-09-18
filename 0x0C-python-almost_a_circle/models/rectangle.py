#!/usr/bin/python3

"""rectangle.py

This module defines the Rectangle class, a subclass of the Base class,
representing rectangles with various properties.

Classes:
    Rectangle: A class representing rectangles.

Attributes:
    None

Methods:
    __init__(self, width, height, x=0, y=0, id=None): Initializes a Rectangle
    instance with specified attributes.
    width(self): Getter method for the width attribute.
    width(self, value): Setter method for the width attribute.
    height(self): Getter method for the height attribute.
    height(self, value): Setter method for the height attribute.
    x(self): Getter method for the x-coordinate attribute.
    x(self, value): Setter method for the x-coordinate attribute.
    y(self): Getter method for the y-coordinate attribute.
    y(self, value): Setter method for the y-coordinate attribute.
    area(self): Calculates and returns the area of the rectangle.
    display(self): Displays the rectangle using the Turtle graphics module.
    update(self, *args, **kwargs): Updates the attributes of the rectangle.
    __str__(self): Returns a string representation of the rectangle.
    to_dictionary(self): Returns a dictionary representation of the rectangle.

"""

from logging import log
import sys
from models.base import Base


class Rectangle(Base):
    """A class representing rectangles.

    Attributes:
        id (int): The identifier for the rectangle.
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the rectangle.
        __y (int): The y-coordinate of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Initializes a
        Rectangle instance with specified attributes.
        width(self): Getter method for the width attribute.
        width(self, value): Setter method for the width attribute.
        height(self): Getter method for the height attribute.
        height(self, value): Setter method for the height attribute.
        x(self): Getter method for the x-coordinate attribute.
        x(self, value): Setter method for the x-coordinate attribute.
        y(self): Getter method for the y-coordinate attribute.
        y(self, value): Setter method for the y-coordinate attribute.
        area(self): Calculates and returns the area of the rectangle.
        display(self): Displays the rectangle using the Turtle graphics module.
        update(self, *args, **kwargs): Updates the attributes of the rectangle.
        __str__(self): Returns a string representation of the rectangle.
        to_dictionary(self): Returns a dictionary representation of the
        rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance with specified attributes.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle. Defaults to
            0.
            y (int, optional): The y-coordinate of the rectangle. Defaults to
            0.
            id (int, optional): The identifier for the rectangle. Defaults to
            None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Getter method for the x-coordinate attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for the x-coordinate attribute.

        Args:
            value (int): The x-coordinate value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Getter method for the y-coordinate attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for the y-coordinate attribute.

        Args:
            value (int): The y-coordinate value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle using the Turtle graphics module."""
        w, h = self.__width, self.__height
        print('\n' * self.__y, end='') and self.__y > 0
        for _ in range(h):
            print(' ' * self.__x, end='')
            for _ in range(w):
                print('#', end='')
            print('')

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.

        Notes:
            The method can be used with positional arguments (args) or keyword
            arguments (kwargs).
            When using positional arguments, the following order should be
            followed:
                1. id
                2. width
                3. height
                4. x
                5. y
            If an attribute is not provided, its value remains unchanged.

        Example:
            To update the width and height:
                rectangle.update(10, 20)
            To update the x and y coordinates using keyword arguments:
                rectangle.update(x=5, y=5)

        """
        attribute_names = ['id', 'width', 'height', 'x', 'y']
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
                    raise TypeError(k + ' must be an integer')
                if k in ['height', 'width'] and kwargs[k] <= 0:
                    raise ValueError(k + ' must be > 0')
                if kwargs[k] < 0:
                    raise ValueError(k + ' must be >= 0')

            self.__width = kwargs.get('width') or self.__width
            self.__height = kwargs.get('height') or self.__height
            self.__x = kwargs.get('x') or self.__x
            self.__y = kwargs.get('y') or self.__y

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def to_dictionary(self):
        """Returns a dictionary representation of the rectangle.

        Returns:
            dict: A dictionary representing the attributes of the rectangle.
        """
        return {
            "x": self.x, "y": self.y, "id": self.id,
            "height": self.height, "width": self.width
        }
