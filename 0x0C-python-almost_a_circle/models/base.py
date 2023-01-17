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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string of list_objs to a file.
        @list_objs: a list of instances who inherits from Base.
        """

        # Create an empty list to hold the JSON string
        json_list = []

        # Check if list of instance is empty
        if list_objs is None:

            # Save an empty list
            with open(cls.__name__ + ".json", "w", encoding='utf-8') as f:
                f.write(str(json_list))

        # List is not empty
        else:

            # Iterate through each object in the list
            for item in list_objs:

                # Get dict representation and append to json_list
                json_list.append(item.to_dictionary())

            # Convert dict representation to JSON string
            json_str = cls.to_json_string(json_list)

            # Write the JSON string to file
            with open(cls.__name__ + ".json", "w", encoding='utf-8') as f:
                f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        List of JSON string representation.
        @json_string: a string representing a list of dictionaries.
        """

        # Create an empty list
        my_list = []

        # Check if json_string is empty
        if json_string is None:
            return my_list

        # json_string is not empty
        my_list = json.loads(json_string)
        return my_list

    @classmethod
    def create(cls, **dictionary):
        """
        Instance with all attributes already set.
        @dictionary: a double pointer to a dictionary.
        """

        # Create Rectangle instance with dummy attributes
        if cls.__name__ == "Rectangle":
            new = cls(1, 2)

        # Create Square instance with dummy attributes
        elif cls.__name__ == "Square":
            new = cls(1)

        # Call update instance method
        new.update(**dictionary)

        return new
