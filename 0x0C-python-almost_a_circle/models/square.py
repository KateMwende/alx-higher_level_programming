#!/usr/bin/python3
"""A class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square class"""

        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter to weight and height
        Args:
            value: value for size
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.weight = value
        self.height = value
