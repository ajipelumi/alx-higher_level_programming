#!/usr/bin/python3
""" Adds a new attribute to an object if its possible. """


def add_attribute(a, key="", value=""):
    """ Adds a new attribute to an object. """
    # Can't attribute to an immutable object
    if isinstance(a, (str, tuple, int, float, bool)):
        raise TypeError("can't add new attribute")

    # Set attribute with setattr built-in
    setattr(a, key, value)
