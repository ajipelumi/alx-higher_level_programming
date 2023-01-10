#!/usr/bin/python3
""" Rectangle class that inherits from BaseGeometry. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines a rectangle. """
    def __init__(self, width, height):
        """ Initializes the data. """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Area of a rectangle. """
        return self.__width * self.__height

    def __str__(self):
        """ Returns a string to print to STDOUT. """
        str = f'[{self.__class__.__name__}] {self.__width}/{self.__height}'
        return str
