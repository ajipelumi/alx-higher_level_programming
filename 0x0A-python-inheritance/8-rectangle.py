#!/usr/bin/python3
""" Rectangle class that inherits from BaseGeometry. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines a rectangle. """
    def __init__(self, width, height):
        """ Initializes the data. """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
