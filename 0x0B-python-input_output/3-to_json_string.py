#!/usr/bin/python3
""" Get the JSON representation of an object (string). """
import json


def to_json_string(my_obj):
    """
    JSON representation of an object (string).
    @my_obj: object to be parsed
    Return: the JSON representation.
    """
    obj = json.dumps(my_obj)
    return obj
