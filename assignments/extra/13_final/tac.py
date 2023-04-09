#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-04-09
Purpose: Assignment 13
"""
import os.path
import sys
import argparse


class TextFile:
    """
    A textfile for manipulation
    """
    def __init__(self, source: str):
        """
        A textfile for manipulation
        :param source: name of a textfile
        """
        self._source = source
        self._lines = []

    @property
    def lines(self) -> []:
        """
        Lines of the file
        :return:
        """
        return self._lines

    def read(self):
        """
        Read the contents of the file
        """
        with open(self._source, "r", encoding="UTF-8)") as _file:
            self._lines = _file.read().splitlines()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment 13: Tac',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input', metavar='FILE', type=str, nargs="+")

    parser.add_argument('-o',
                        '--outfile',
                        type=str,
                        required=False,
                        default=sys.stdout.name)

    arguments = parser.parse_args()

    # Check to see if the input file(s) are there
    for file in arguments.input:
        if not os.path.isfile(file):
            print(f"No such file or directory: '{file}'")
            sys.exit(-1)

    if arguments.outfile == sys.stdout.name:
        outfile = sys.stdout
    else:
        outfile = open(arguments.outfile, "w", encoding="UTF-8")

    for file in arguments.input:
        text = TextFile(file)
        text.read()
        for item in reversed(text.lines):
            outfile.write(f"{item}\n")

    sys.exit(0)
