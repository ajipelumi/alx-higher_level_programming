#!/usr/bin/python3
""" Module returns a find_peak function. """


def fpeak(my_list, low, high):
    """ Recursion to find peak. """
    mid = (low + (high - low) // 2)
    if mid == 0 and my_list[mid] >= my_list[mid + 1]:
        return my_list[mid]
    elif mid == (high - 1) and my_list[mid] >= my_list[mid - 1]:
        return my_list[mid]
    elif mid > 0 and my_list[mid - 1] > my_list[mid]:
        return fpeak(my_list, low, mid - 1)
    else:
        return fpeak(my_list, mid + 1, high)


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]

    return fpeak(list_of_integers, 0, length - 1)
