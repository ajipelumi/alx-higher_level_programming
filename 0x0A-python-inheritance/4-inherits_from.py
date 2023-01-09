#!/usr/bin/python3
""" Checks if the object is an instance inherited
(directly or indirectly) from the specified class. """


def inherits_from(obj, a_class):
    """
    checks for subclass
    obj: object/instance to check
    a_class: specified class
    return: True if the object is a subclass of
    specified class, otherwise False.
    """
    # get all relevant classes in method-resolution order
    mro = type(obj).mro()
    mro.pop(0)  # a class is a subclass of itself so we pop it
    if a_class in mro:
        return True
    else:
        return False
