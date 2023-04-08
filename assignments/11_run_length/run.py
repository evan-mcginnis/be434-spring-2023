#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-04-07
Purpose: Assignment 11
"""
import os.path
import sys
import argparse


class Sequence:
    """
    A DNA Sequence
    """
    def __init__(self, uncompressed: str):
        """
        The sequence -- the parameter can be the actual sequence or a file
        containing one or more sequences
        :param uncompressed: sequence or file of sequences
        """
        self._raw = []
        if os.path.isfile(arguments.str):
            with open(uncompressed, "r", encoding="UTF-8") as file:
                self._uncompressed = [x.split() for x in file.readlines()]
        else:
            self._uncompressed = [[uncompressed]]

        self._compressed = ""

    @property
    def uncompressed(self) -> []:
        """
        The uncompressed sequences
        :return:
        """
        return self._uncompressed

    def compress(self) -> str:
        """
        RLE Compression of the current sequence or sequences
        :return:
        """
        count = 1
        element_no = 0
        for element in self._uncompressed:
            for index in range(len(element[0]) - 1):
                if element[0][index] == element[0][index + 1]:
                    count += 1
                else:
                    if count > 1:
                        self._compressed += element[0][index]
                        self._compressed += str(count)
                        count = 1
                    else:
                        count = 1
                        self._compressed += element[0][index]
            self._compressed += element[0][-1]
            if count > 1:
                self._compressed += str(count)
            # So the tests will pass, don't put a newline on the final line
            if element_no != len(self._uncompressed) - 1:
                self._compressed += "\n"
            element_no += 1
            count = 1

        return self._compressed

    def save(self):
        """
        Save the compressed sequence to a file
        """
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment 11: Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # A note to the grader:
    # I do not agree with the choice made here: sometimes the positional
    # argument is to be interpreted, sometimes it is a file?
    # This can lead to all sorts of problems -- let's say you had a file
    # named AA -- ambiguous what the correct behavior is.

    # Consider making this one way or another or even implement this as a pipe
    # like so cat ./inputs/foo.txt | ./run/py

    parser.add_argument('str', metavar='str', type=str)

    arguments = parser.parse_args()

    sequence = Sequence(arguments.str)
    print(f"{sequence.compress()}")
    sequence.save()

    sys.exit(0)
