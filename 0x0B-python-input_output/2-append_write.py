#!/usr/bin/pyhon3
"""Append a string"""


def append_write(filename="", text=""):
    """Append a file
    Args:
        filename: File to be appended a string
        text: text to add to filename
    """

    with open(filename, 'a', encoding='utf-8') as f:
        str_p = f.write(text)

    return (str_p)
