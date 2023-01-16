#!/usr/bin/python3
""" Base of all other classes. """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON string representation of list_dictionaries.
        @list_dictionaries: a list of dictionaries.
        """

        # Check if list_dictionaries is empty
        if list_dictionaries is None:
            return "[]"

        # list_dictionaries is not empty
        my_list = json.dumps(list_dictionaries)
        return my_list
