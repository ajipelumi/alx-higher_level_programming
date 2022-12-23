#!/usr/bin/python3
""" This module defines a magic class. """


class MagicClass:
    """ Define a magic class """
    def __init__(self, radius):
        """ Initialize data. """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.radius = radius

    def area(self):
        """ Area. """
        return (self.radius ** 2) * math.pi

    def circumference(self):
        """ Circumference. """
        return (2 * math.pi) * self.radius
