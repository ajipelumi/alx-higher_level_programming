#!/usr/bin/python3
""" Save to a JSON file. """
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.
    @my_obj: object to be parsed
    @filename: text file
    Return: None.
    """
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
