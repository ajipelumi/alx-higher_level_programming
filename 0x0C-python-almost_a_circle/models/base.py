#!/usr/bin/python3
""" Base of all other classes. """


class Base:
    """ Base class. """
    __nb_objects = 0  # Class attribute

    def __init__(self, id=None):
        """ Initialize data. """
        # Check if an integer is entered
        if id is not None:
            self.id = id

        # No integer is found
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
