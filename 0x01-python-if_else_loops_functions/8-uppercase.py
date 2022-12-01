#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        char = ord(letter)  # get character ASCII
        if char >= 97 and char <= 122:  # character is lowercase
            letter = chr(char - 32)  # convert to uppercase and to character
        print("{}".format(letter), end='')  # print character
    print()  # print newline
