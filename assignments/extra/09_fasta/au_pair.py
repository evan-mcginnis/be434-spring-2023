#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-04-09
Purpose: Assignment 13
"""
import os.path
import sys
import argparse

from Bio import SeqIO

FORMAT = "fasta"
END_EVEN = "_2"
END_ODD = "_1"


class Fasta:
    """

    """
    def __init__(self, file: str):
        """

        :param file:
        """
        self._file = file
        self._fasta = SeqIO.FastaIO.FastaTwoLineIterator
        self._odds = []
        self._evens = []
        self._records = []

    def read(self):
        """
        Read the FASTA format file
        """
        self._fasta = SeqIO.parse(self._file, FORMAT)
        for record in self._fasta:
            self._records.append(record)

    def odds(self) -> []:
        """
        The odd number seqences
        :return:
        """
        sequences = []
        i = 1
        for seq in self._records:
            if not (i % 2) == 0:
                sequences.append(seq)
            i += 1
        return sequences

    def evens(self) -> []:
        """
        The even number sequences
        :return:
        """
        sequences = []
        i = 1
        for seq in self._records:
            if (i % 2) == 0:
                sequences.append(seq)
            i += 1
        return sequences

    def write(self, file: str, sequences: []):
        SeqIO.write(sequences, file, FORMAT)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment Extra 09: fasta',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input', metavar='FILE', type=str, nargs="+")

    parser.add_argument('-o',
                        '--outdir',
                        type=str,
                        metavar='DIR',
                        required=False,
                        default='split')

    arguments = parser.parse_args()

    # Check to see if the input file(s) are there
    for file in arguments.input:
        if not os.path.isfile(file):
            print(f"No such file or directory: '{file}'")
            sys.exit(-1)

    if not os.path.isdir(arguments.outdir):
        os.mkdir(arguments.outdir)

    for file in arguments.input:
        sequences = Fasta(file)
        sequences.read()
        outbase = os.path.basename(file)
        filename = os.path.splitext(outbase)
        sequences.write(
            arguments.outdir + os.path.sep + filename[0] + "_1" + filename[1],
            sequences.odds())
        sequences.write(
            arguments.outdir + os.path.sep + filename[0] + "_2" + filename[1],
            sequences.evens())

    print(f'Done, see output in "{arguments.outdir}"')

    sys.exit(0)
