#!/usr/bin/python3
""" Module returns a find_peak function. """


def fpeak(my_list, low, high):
    """ Recursion to find peak. """
    # Find middle element
    mid = (low + (high - low) // 2)

    # If mid is first/last element and not smaller than neighbouring element
    if (mid == 0 or my_list[mid - 1] <= my_list[mid]) and \
            (mid == len(my_list) - 1 or my_list[mid + 1] <= my_list[mid]):
        return my_list[mid]

    # Check if mid is smaller than left element
    elif mid > 0 and my_list[mid - 1] > my_list[mid]:
        return fpeak(my_list, low, mid - 1)

    # Mid is smaller than right element
    else:
        return fpeak(my_list, mid + 1, high)


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers."""
    # List of integers is empty
    if not list_of_integers:
        return None

    # Get length of list
    length = len(list_of_integers)

    # Check if list contains just one element
    if length == 1:
        return list_of_integers[0]

    # Call recursive fpeak
    return fpeak(list_of_integers, 0, length - 1)
