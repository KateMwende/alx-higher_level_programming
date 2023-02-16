#!/usr/bin/python3
"""Base class module"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class initialization
        Args:
            id: public instance attribute
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        else:
            self.id = id
