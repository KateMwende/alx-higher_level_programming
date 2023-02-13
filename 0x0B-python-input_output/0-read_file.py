#!/usr/bin/python3
"""A function that reads a text file (UTF8) and prints it to stdout"""

def read_file(filename=""):
    """Function that reads a file and prints to stdout
    Args:
        filename: File to read
    """

    with open(filename encoding='utf-8') as f:
        for line in f:
            print(line, end='')
