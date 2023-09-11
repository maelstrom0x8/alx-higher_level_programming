Base = __import__('7-base_geometry').Base

class BaseGeometry:

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
