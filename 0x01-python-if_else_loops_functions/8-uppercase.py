#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:  # lowercase character
            letter = chr(ord(letter) - 32)  # convert to uppercase
        print("{}".format(letter), end="")
    print()  # print newline
