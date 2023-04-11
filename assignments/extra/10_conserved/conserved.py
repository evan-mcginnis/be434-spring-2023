#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-04-10
Purpose: Assignment 10 extra
"""
import os.path
import sys
import argparse

MATCH = "|"
MISMATCH = "X"


class Common:
    """
    Find subsequences in common
    """
    def __init__(self, file: str):
        """
        Find subsequences in common
        :param file: Name of the to read
        """
        self._inCommon = []
        self._lines = []
        self._file = file

    @property
    def lines(self) -> []:
        """
        Lines read from file
        :return: lines as list
        """
        return self._lines

    def read(self):
        """
        Read lines from file
        """
        with open(self._file, "r", encoding="UTF=8") as file:
            self._lines = file.readlines()

    def createCommonMap(self) -> []:
        """
        Create a list with X indicating mismatch for position, | inditating
        match.
        :return: list of match indications
        """
        # The problem here is that the strings may not be the same length
        # so we need to find the shortest one, although it looks like
        # the test data has equal length for all strings
        shortest = min(self._lines, key=len)
        # Initialize the differences
        for i in range(len(shortest) - 1):
            self._inCommon.append('X')

        # Step through each position
        for i in range(len(shortest) - 1):
            matched = False
            differenceDetected = False
            # Step through each line -- the first always matches itself
            for j in range(1, len(self._lines)):
                matched = (self._lines[j][i] == self._lines[0][i])
                if not matched:
                    differenceDetected = True
            if not differenceDetected:
                self._inCommon[i] = MATCH
            else:
                self._inCommon[i] = MISMATCH
        return self._inCommon


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment Extra 10: Conserved',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input', metavar='FILE', type=str)

    arguments = parser.parse_args()

    # Check to see if the input file(s) are there
    if not os.path.isfile(arguments.input):
        print(f"No such file or directory: '{arguments.input}'")
        sys.exit(-1)

    c = Common(arguments.input)
    c.read()
    inCommon = c.createCommonMap()
    for line in c.lines:
        sys.stdout.write(f"{line}")
    print(f"{''.join(inCommon)}")

    sys.exit(0)
