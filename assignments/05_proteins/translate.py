#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-02-25
Purpose: Assignment 5
"""

import argparse
import sys
import csv

class Codons:
    def __init__(self, filename: str):
        self._filename = filename
        self._translations = {}

    @property
    def filename(self) -> str:
        return self._filename

    def read(self) -> bool:
        try:
            with open(self._filename) as f:
                for line in f:
                    (key, val) = line.split()
                    self._translations[key] = val
            rc = True
        except FileNotFoundError:
            print(f'No such file or directory: \'{self._filename}\'')
            rc = False
        return rc

    def translate(self, sequence: str):
        translation = ""
        x = 3
        codon_list = [sequence[y - x:y] for y in range(x, len(sequence) + x, x)]
        for codon in codon_list:
            try:
                translation += self._translations[codon]
            except KeyError as err:
                translation += '-'
        return translation

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment 5: Translate a given DNA/RNA sequence to amino acids',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c', '--codons', required=True, type=str)
    parser.add_argument('-o', '--output', required=False, type=str, default="out.txt")
    parser.add_argument('sequence', metavar='str', type=str, help="")

    arguments = parser.parse_args()

    c = Codons(arguments.codons)
    if not c.read():
        parser.print_usage()
        sys.exit(-1)

    with open(arguments.output, 'w') as f:
        f.write(c.translate(arguments.sequence.upper()))

    print(f'Output written to "{arguments.output}".')


