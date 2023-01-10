#!/usr/bin/python3
""" Square class that inherits from Rectangle. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class. """
    def __init__(self, size):
        """ Initialize data. """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Area of a square. """
        return self.__size ** 2

    def __str__(self):
        """ Returns a string to print to STDOUT. """
        str = f'[Square] {self.__size}/{self.__size}'
        return str
