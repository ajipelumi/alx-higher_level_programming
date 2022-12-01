#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            letter = chr(ord(letter) - 32)  # convert to uppercase
        print("{}".format(letter), end="")
    print()  # print newline
