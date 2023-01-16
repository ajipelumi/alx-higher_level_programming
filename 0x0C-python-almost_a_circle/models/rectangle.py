#!/usr/bin/python3
""" Rectangle class. """


class Rectangle(Base):
    """ Rectangle class that inherits from Base. """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize data. """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Retrieve width. """
        return self.__width

    @width.setter
    def width(self, width):
        """ Set property. """
        self.__width = width

    @property
    def height(self):
        """ Retrieve height. """
        return self.__height

    @height.setter
    def height(self, height):
        """ Set property. """
        self.__height = height

    @property
    def x(self):
        """ Retrieve x. """
        return self.__x

    @x.setter
    def x(self, x):
        """ Set property. """
        self.__x = x

    @property
    def y(self):
        """ Retrieve y. """
        return self.__y

    @y.setter
    def y(self, y):
        """ Set property. """
        self.__y = y
