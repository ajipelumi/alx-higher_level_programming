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
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """ Retrieve height. """
        return self.__height

    @height.setter
    def height(self, height):
        """ Set property. """
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """ Retrieve x. """
        return self.__x

    @x.setter
    def x(self, x):
        """ Set property. """
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """ Retrieve y. """
        return self.__y

    @y.setter
    def y(self, y):
        """ Set property. """
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """ Area of a rectangle. """
        return self.width * self.height

    def display(self):
        """ Prints character '#' to stdout."""
        for i in range(self.y):
            print(" ")
        for i in range(self.height):
            print("{}{}".format(' ' * self.x, '#' * self.width))

    def __str__(self):
        """ Define string representation of Rectangle class. """
        # Reassign variables to avoid pycodestyle error
        x = self.x
        y = self.y
        width = self.width
        height = self.height

        buf = f'[Rectangle] ({self.id}) {x}/{y} - {width}/{height}'
        return buf

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute. """
        attr = ('id', 'width', 'height', 'x', 'y')

        # Assign each element of args to attr
        for i in range(len(attr)):
            if i < len(args):
                setattr(self, attr[i], args[i])

        # Assign value to key
        for key, value in kwargs.items():
            setattr(self, key, value)
