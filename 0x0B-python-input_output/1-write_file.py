#!/usr/bin/python3
""" Writes a string to a text file (UTF8). """


def write_file(filename="", text=""):
    """
    Writes a string to a text file.
    @filename: text file
    @text: string to be parsed
    Return: the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        num = f.write(text)
    return num
