#!/usr/bin/python3
""" Creates a class MyList that inherits from list. """


class MyList(list):
    """ Inherits from list. """

    def print_sorted(self):
        """ Prints the list, but sorted (ascending sort). """
        print(sorted(self))
