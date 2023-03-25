#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-03-24
Purpose: Assignment 8
"""

import argparse
import sys
from pathlib import Path
from operator import countOf


class Kmer:
    def __init__(self, file: str):
        self._strings = []
        self._exploded = []
        self._file = file

    def read(self):
        """
        Read in the file and convert all lines to a single list
        """
        with open(self._file) as file:
            self._strings = file.read().replace('\n', ' ').split()

    def occurences(self, kmer: str) -> int:
        """
        The number of occurences of the string
        :param kmer: The string
        :return: count of the occurences
        """
        return countOf(self._exploded, kmer)

    def find_common(self, kmers) -> []:
        set1 = set(self._exploded)
        set2 = set(kmers.exploded)
        intersection = set1.intersection(set2)
        # print("Intersection: {}".format(intersection))
        return intersection

    def generate_all_substrings(self, k: int):
        for sub in self._strings:
            res = []
            for i in range(len(sub) - k + 1):
                res.append(sub[i:i + k])
            self._exploded.extend(res)

    def __str__(self):
        return str(self._exploded)

    @property
    def strings(self) -> []:
        return self._strings

    @property
    def exploded(self) -> []:
        return self._exploded


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment 8: kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-k', '--kmer',
                        required=False,
                        type=int,
                        default=3,
                        help="K-mer size")
    parser.add_argument('file', metavar='FILE', type=str, nargs=2)

    arguments = parser.parse_args()

    # Check to see if the files are there
    for file in arguments.file:
        target = Path(file)
        if not target.is_file():
            print(f"No such file or directory: '{file}'")
            sys.exit(-1)

    # Check to see that kmers is a positive value
    if arguments.kmer <= 0:
        parser.error(f'--kmer "{arguments.kmer}" must be > 0')

    # Read in the files
    left = Kmer(arguments.file[0])
    left.read()
    left.generate_all_substrings(arguments.kmer)

    right = Kmer(arguments.file[1])
    right.read()
    right.generate_all_substrings(arguments.kmer)

    # Find the intersection between the two
    in_common_text = right.find_common(left)

    for com in in_common_text:
        print(f"{com:11}{left.occurences(com):5}{right.occurences(com):6}")



