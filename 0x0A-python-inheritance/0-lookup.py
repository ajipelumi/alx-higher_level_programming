#!/usr/bin/python3
""" Returns the list of available attributes and methods of an object. """


def lookup(obj):
    """
    gets the attributes and methods of an object with dir.
    obj: object to be scanned
    return a list of the attributes and objects
    """
    return list(dir(obj))
