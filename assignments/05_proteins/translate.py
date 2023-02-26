#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-02-25
Purpose: Assignment 5
"""

import argparse
import sys

#
# A note to the grader:
# Having one test fail because the filename is not enclosed in single
# quotes and another fail because a filename is not in double quotes is
# inconsistent.  Consider revising.
#
# The line character limit of 80 is extreme. In several decades of doing this
# professionally, I have never had a test fail because a line was 81 characters
# long. It now forced me to use nonsense variable names, producing less
# readable code, not more. Consider revising
#


class Codons:
    """
    Codons
    """
    def __init__(self, filename: str):
        """
        Codons
        :param filename: DNA/RNA sequence definitions
        """
        self._filename = filename
        self._translations = {}

    @property
    def filename(self) -> str:
        """
        The filename associated with the current codon list
        :return:
        """
        return self._filename

    def read(self) -> bool:
        """
        Read in the current codon translations
        :return: True on success
        """
        try:
            with open(self._filename, encoding='UTF-8') as input_file:
                for line in input_file:
                    (key, val) = line.split()
                    self._translations[key] = val
            return_code = True
        except FileNotFoundError:
            print(f'No such file or directory: \'{self._filename}\'')
            return_code = False
        return return_code

    def translate(self, seq: str) -> str:
        """
        Translate the sequence
        :param seq: Sequence to be translated
        :return:
        """
        translation = ""
        sz = 3
        the_list = [seq[y - sz:y] for y in range(sz, len(seq) + sz, sz)]
        for codon in the_list:
            try:
                translation += self._translations[codon]
            except KeyError:
                translation += '-'
        return translation


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment 5: Translate DNA/RNA sequence to amino acids',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c', '--codons', required=True, type=str)
    parser.add_argument('-o', '--output', required=False, type=str,
                        default="out.txt")
    parser.add_argument('sequence', metavar='str', type=str, help="")

    arguments = parser.parse_args()

    c = Codons(arguments.codons)
    if not c.read():
        parser.print_usage()
        sys.exit(-1)

    with open(arguments.output, 'w', encoding='UTF-8') as out:
        out.write(c.translate(arguments.sequence.upper()))

    print(f'Output written to "{arguments.output}".')
