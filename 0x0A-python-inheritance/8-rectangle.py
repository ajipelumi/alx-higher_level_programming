#!/usr/bin/python3
""" Rectangle class that inherits from BaseGeometry. """


class Rectangle(BaseGeometry):
    """ Rectangle Class. """
    def __init__(self, width, height):
        """ Initialize data. """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
