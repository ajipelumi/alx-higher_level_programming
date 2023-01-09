#!/usr/bin/python3
""" Checks if the object is an instance of the specified class. """


def is_kind_of_class(obj, a_class):
    """
    checks for instance of an object
    obj: object/instance to check
    a_class: specified class
    return: True if the object is an instance, otherwise False.
    """
    return isinstance(obj, a_class)
