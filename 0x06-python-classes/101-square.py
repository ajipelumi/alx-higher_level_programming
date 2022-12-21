#!/usr/bin/python3
""" This module defines a square. """


class Square:
    """ Defines a square. """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes the data. """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Retrieve size. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set property. """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """ Retrieve position. """
        return self.__position

    @position.setter
    def position(self, value):
        """ Set property. """
        self.__position = value
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        i, j = value
        if type(i) != int or type(j) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if i < 0 or j < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Returns the current square area. """
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout the square with the character #. """
        num = self.__size
        pos = self.__position
        if num == 0:
            print("")
            return
        for i in range(num):
            count = 0
            for j in range(num):
                for k in range(pos[0]):
                    if count is not pos[0]:
                        print(" ", end="")  # fill with spaces
                count = pos[0]
                print("#", end="")
            print()

    def __str__(self):
        return str(self.my_print())
