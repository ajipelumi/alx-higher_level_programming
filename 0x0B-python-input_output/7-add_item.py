#!/usr/bin/python3

from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
import sys


# Create a list
my_list = []

# Get length of arguments passed
arg_len = len(sys.argv)

# Loop through arg and append command line arguments to list
for item in range(1, arg_len):
    my_list.append(sys.argv[item])

file = "add_item.json"  # JSON file

# Get object from JSON file
try:
    # file exists so we get objects from JSON file
    obj = load_from_json_file(file)
    # Append new arguments to returned object
    new_list = obj + my_list
    # Save the new list in JSON file
    save_to_json_file(new_list, file)
except Exception:
    # file does not exist so save our arguments to JSON file
    save_to_json_file(my, file)
