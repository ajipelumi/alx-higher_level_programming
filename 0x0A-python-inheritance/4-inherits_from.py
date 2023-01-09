#!/usr/bin/python3
""" Checks if the object is an instance inherited
(directly or indirectly) from the specified class. """


def inherits_from(obj, a_class):
    """
    checks for inheritance
    obj: object/instance to check
    a_class: specified class
    return: True if the object is an instance inherited
    (directly or indirectly), otherwise False.
    """
    return issubclass(type(obj), a_class)
