#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-04-08
Purpose: Assignment 12
"""
import os.path
import sys
import argparse
import re


class TextFile:
    """
    A textfile for manipulation and searching
    """
    def __init__(self, source: str):
        """
        A textfile for manipulation and searching
        :param source: name of a textfile
        """
        self._source = source
        self._lines = []
        self._insensitive = False

    @property
    def insensitive(self) -> bool:
        """
        Case insensitive flag
        :return:
        """
        return self._insensitive

    @insensitive.setter
    def insensitive(self, insensitive: bool):
        """
        Set the case insensitive flag
        :param insensitive: Boolean indicating case sensitivity
        """
        self._insensitive = insensitive

    def read(self):
        """
        Read the contents of the file
        """
        with open(self._source, "r", encoding="UTF-8)") as _file:
            self._lines = _file.read().splitlines()

    def match(self, pattern: str) -> []:
        """
        Match the file to the regular expression pattern
        :param pattern: regular expression
        :return: list of matches
        """
        matched = []
        for line in self._lines:
            # This is odd -- the value re.NOFLAG should be used here, but
            # python claims re does not have that attribute
            text = re.search(pattern, line,
                             re.IGNORECASE if self._insensitive else re.A)
            if text is not None:
                matched.append(line)
        return matched


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment 12: Grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern', metavar='PATTERN', type=str)
    parser.add_argument('input', metavar='FILE', type=str, nargs="+")

    parser.add_argument('-i',
                        "--insensitive",
                        action="store_true",
                        required=False,
                        default=False)

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
        text.insensitive = arguments.insensitive
        text.read()
        matched = text.match(arguments.pattern)
        for line in matched:
            if len(arguments.input) > 1:
                outfile.write(f"{file}:{line}\n")
            else:
                outfile.write(f"{line}\n")
    sys.exit(0)
