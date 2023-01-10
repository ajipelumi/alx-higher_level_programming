#!/usr/bin/python3
""" Appends a string at the end of a text file (UTF8). """


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file.
    @filename: text file
    @text: string to be parsed
    Return: the number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        num = f.write(text)
    return num
