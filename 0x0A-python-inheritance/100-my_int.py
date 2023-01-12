#!/usr/bin/python3
""" Class inherits from int. """


class MyInt(int):
    """ MyInt class."""

    def __eq__(self, other):
        """ Comparison operators. """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Comparison operators. """
        return int.__eq__(self, other)
