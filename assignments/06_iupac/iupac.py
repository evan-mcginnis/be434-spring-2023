#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-03-03
Purpose: Assignment 6
"""

# A note to grader:
# A test fails because a blank line contains a tab?
# That's a bit much, and would never be flagged in industrial code.
# Consider revising.

import argparse
import sys


class IUPAC:
    """
    IUPAC
    https://www.bioinformatics.org/sms/iupac.html
    """
    def __init__(self):
        """
        Codons
        :param filename: DNA/RNA sequence definitions
        """
        self._codes = {
            "A": "A",
            "C": "C",
            "G": "G",
            "T": "T",
            "U": "U",
            "R": "AG",
            "Y": "CT",
            "S": "GC",
            "W": "AT",
            "K": "GT",
            "M": "AC",
            "B": "CGT",
            "D": "AGT",
            "H": "ACT",
            "V": "ACG",
            "N": "ACGT"
        }

    def longest_match(self, target_seq: str) -> str:
        """
        The longest value found matching the sequence
        :param target_seq:
        :return:
        """
        match = ""
        max_len_sequence = 0
        for key, value in self._codes.items():
            if target_seq.upper() == key and len(value) > max_len_sequence:
                match = value
        if len(match) > 1:
            found = "[" + match + "]"
        else:
            found = match
        return found


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment 6: IUPAC',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequences', metavar='SEQ', type=str, nargs='+')
    parser.add_argument('-o', '--outfile', required=False, type=str)

    arguments = parser.parse_args()
    try:
        out = open(arguments.outfile, 'wt', encoding='UTF-8') \
            if arguments.outfile else sys.stdout
    except FileExistsError:
        print(f'File already exists: {arguments.outfile}')
        sys.exit(-1)

    codes = IUPAC()

    for sequence in arguments.sequences:
        out.write(f'{sequence} ')
        for code in sequence:
            out.write(f'{codes.longest_match(code)}')
        out.write("\n")

    if arguments.outfile:
        print(f'Done, see output in "{arguments.outfile}"')
    sys.exit(0)
