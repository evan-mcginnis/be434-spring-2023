#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-04-05
Purpose: Assignment 10
"""
import os.path
import sys
import argparse


class Common:
    """
    Common strings in two files
    """
    def __init__(self, file1: str, file2: str):
        """
        Common strings in two files
        :param file1: A text file
        :param file2: A text file
        """
        self._left = file1
        self._right = file2
        self._left_contents = []
        self._right_contents = []
        self._left_set = set([])
        self._right_set = set([])

    def read(self):
        """
        Read the files
        """
        with open(self._left, "r", encoding="UTF-8") as file:
            lines = [x.split() for x in file.readlines()]
            for line in lines:
                self._left_contents.extend(line)
            self._left_set = set(self._left_contents)
        with open(self._right, "r", encoding="UTF-8") as file:
            lines = [x.split() for x in file.readlines()]
            for line in lines:
                self._right_contents.extend(line)
            self._right_set = set(self._right_contents)

    def in_common(self) -> []:
        """
        Find the strings the two files have in common
        :return: Sorted list of intersection
        """
        return sorted(self._left_set.intersection(self._right_set))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment 10: Common Words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', metavar='FILE', type=str, nargs=2)

    parser.add_argument('-o', '--outfile',
                        required=False,
                        type=str,
                        help="Output file")

    arguments = parser.parse_args()

    # Check file access
    for _file in arguments.file:
        if not os.path.isfile(_file):
            print(f"No such file or directory: '{_file}'")
            sys.exit(2)

    if arguments.outfile is not None:
        outfile = open(arguments.outfile, "w", encoding="UTF-8")
    else:
        outfile = sys.stdout

    common = Common(arguments.file[0], arguments.file[1])
    common.read()

    words_in_common = common.in_common()

    for word in words_in_common:
        outfile.write(f"{word}\n")

    sys.exit(0)
