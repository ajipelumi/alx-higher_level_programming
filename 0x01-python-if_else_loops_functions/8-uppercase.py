#!/usr/bin/python3
def uppercase(str):
    lent = len(str)  # get string length
    for i in range(0, lent):
        c = str[i]  # get character
        if ord(c) >= 97 and ord(c) <= 122:  # character is lowercase
            c = ord(c) - 32  # convert to uppercase
            print("{0:c}".format(c), end='')  # print character
        else:  # character is not lowercase
            print("{0}".format(c), end='')
