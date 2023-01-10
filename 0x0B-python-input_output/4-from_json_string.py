#!/usr/bin/python3
""" Get the Python representation of a JSON (string). """
import json


def from_json_string(my_str):
    """
    Python representation of an object (string).
    @my_str: object to be parsed
    Return: the Python representation.
    """
    obj = json.loads(my_str)
    return obj
