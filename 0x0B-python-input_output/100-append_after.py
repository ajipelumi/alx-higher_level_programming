#!/usr/bin/python3
""" Inserts a line of text to a file. """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line
    containing a specific string.
    """
    # Open file and read lines into memory with readlines()
    with open(filename, "r", encoding='utf-8') as f:
        lines = f.readlines()
    # Open file again but with write access
    with open(filename, "w", encoding='utf-8') as f:
        for line in lines:
            # Write back into file line ny line
            f.write(line)
            # Specific string found in line
            if search_string in line:
                # Write new string after the line
                f.write(new_string)
