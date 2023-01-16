#!/usr/bin/python3
""" Square class. """


class Square(Rectangle):
    """ Square class that inherits from Rectangle. """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize data. """
        # Call super class to initialize attributes
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Retrieve size. """
        return self.width

    @size.setter
    def size(self, size):
        """ Set size property. """
        self.width = self.height = size

    def __str__(self):
        """ Define string representation of Square class."""
        # Reassign to avoid pycodestyle error
        x = self.x
        y = self.y
        size = self.width

        buf = f'[Square] ({self.id}) {x}/{y} - {size}'
        return buf

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute. """
        attr = ('id', 'size', 'x', 'y')

        # Assign each element of args to attr
        for i in range(len(attr)):
            if i < len(args):
                setattr(self, attr[i], args[i])

        # Assign value to key
        for key, value in kwargs.items():
            setattr(self, key, value)
