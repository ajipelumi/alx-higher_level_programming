#!/usr/bin/python3
""" Defines a student. """


class Student:
    """ Student class. """
    def __init__(self, first_name, last_name, age):
        """
        Initialize data.
        @first_name: first name of student
        @last_name: last name of student
        @age: student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance. """
        # Define a dictionary to store items
        my_dict = {}

        # Check for list of keys
        if attrs is None:  # No list found
            return self.__dict__
        else:  # List found
            for item in attrs:  # Iterate through list
                if item in self.__dict__:  # Key found
                    item_dict = {item: self.__dict__[item]}
                    # Update dictionary everytime key is found
                    my_dict.update(item_dict)
            return my_dict
