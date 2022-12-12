#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    returns a list with all values multiplied by a number
    my_list: list to be examined
    number: each value will be multiplied by number
    Return: returns a new list
    """
    # use lambda to apply function to every element of my_list
    result = map(lambda x: x * number, my_list)
    return list(result)
