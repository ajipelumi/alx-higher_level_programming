#!/usr/bin/python3
""" JSON serialization of an object. """
import json


def class_to_json(obj):
    """
    dictionary description with simple data structure
    @obj: is an instance of a Class
    Return: the dictionary description.
    """
    # Get instance attributes/variables with built-in (vars)
    new = json.dumps(obj.__dict__)
    return new
