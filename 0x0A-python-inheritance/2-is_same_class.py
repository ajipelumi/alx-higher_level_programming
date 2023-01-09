#!/usr/bin/python3
""" Checks if the object is exactly an instance of the specified class. """


def is_same_class(obj, a_class):
    """
    checks for instance of an object
    obj: object/instance to check
    a_class: specified class
    return: True if the object is an instance, otherwise False.
    """
    return type(obj) == a_class
