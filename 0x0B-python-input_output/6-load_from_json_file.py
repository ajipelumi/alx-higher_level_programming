#!/usr/bin/python3
""" Creates an Object from a JSON file. """
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.
    @filename: JSON file
    Return: Python object.
    """
    with open(filename, "w", encoding='utf-8') as f:
        obj = json.load(f)
    return obj
