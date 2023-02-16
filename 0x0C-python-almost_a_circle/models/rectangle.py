#!/usr/bin/python3
"""Module for class Rectangle"""


class Rectangle(Base):
    """Class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of Rectangle class"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
