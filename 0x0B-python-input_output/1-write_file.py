#!/usr/bin/python3
"""Function thyat writes a string to a text file (UTF8) and returns
    the number of characters written"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number
    of characters written.
    Args:
        filename: The file to write to
        text: The text to write to filename
    """

    with open(filename, 'w', encoding='utf-8') as f:
        str_p = f.write(text)

    return (str_p)
