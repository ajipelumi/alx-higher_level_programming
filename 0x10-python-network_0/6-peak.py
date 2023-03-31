#!/usr/bin/python3
""" Module returns a find_peak function. """


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers."""
    if list_of_integers is None:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]

    my_list = list_of_integers
    for idx, val in enumerate(my_list):
        if idx == 0 and val >= my_list[idx + 1]:
            return val
        elif idx == (length - 1) and val >= my_list[idx - 1]:
            return val
        elif val >= my_list[idx + 1] and val >= my_list[idx - 1]:
            return val
