#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-03-03
Purpose: Assignment 6
"""
import sys
import argparse
import random


def ranged_type(value_type, min_value, max_value):
    """
    Return function handle of an argument type function for ArgumentParser checking a range:
        min_value <= arg <= max_value

    Parameters
    ----------
    value_type  - value-type to convert arg to
    min_value   - minimum acceptable argument
    max_value   - maximum acceptable argument

    Returns
    -------
    function handle of an argument type function for ArgumentParser


    Usage
    -----
        ranged_type(float, 0.0, 1.0)

    """

    def range_checker(arg: str):
        try:
            f = value_type(arg)
        except ValueError:
            raise argparse.ArgumentTypeError(f'must be a valid {value_type}')
        if f < min_value or f > max_value:
            raise argparse.ArgumentTypeError(f'"{f}" must be between {min_value} and {max_value}')
        return f

    # Return function handle to checking function
    return range_checker

def create_pool(pctgc, max_len, seq_type):
    """ Create the pool of bases """

    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))


class Synthetic:
    def __init__(self, outfile: str, theType: str, numseqs: int, minlen: int, maxlen: int, percent: float):
        self._outfile = outfile
        self._type = theType
        self._numseqs = numseqs
        self._minlen = minlen
        self._maxlen = maxlen
        self._percent = percent
        self._pool = create_pool(arguments.pctgc, arguments.maxlen, arguments.seqtype)

    def write(self) -> bool:
        with open(self._outfile, "w") as sequences:
            for sequence in range(self._numseqs):
                seq_length = random.randint(self._minlen, self._maxlen)
                seq = random.sample(self._pool, seq_length)
                sequences.write(f'>{sequence}\n')
                sequences.write(''.join(seq))
                sequences.write('\n')
        return True



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment 7: Synthetic DNS',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o', '--outfile', required=False, type=str, default="out.fa", help="Output filename")
    parser.add_argument('-t', '--seqtype', required=False, choices=["dna", "rna"], default="dna", type=str, help="dna or rna")
    parser.add_argument('-n', '--numseqs', required=False, default=10, type=int, help="Number of sequences to create")
    parser.add_argument('-m', '--minlen', required=False,  default=50, type=int, help="Minimum length")
    parser.add_argument('-x', '--maxlen', required=False, default=75, type=int, help="Maximum length")

    # This is a bit more flexible way of doing this that the method given in the readme
    # parser.add_argument('-p', '--pctgc', required=False,  type=ranged_type(float, 0, 1), help="Percent GC", default=0.5)

    parser.add_argument('-p', '--pctgc', required=False,  type=float, help="Percent GC", default=0.5)
    parser.add_argument('-s', "--seed", required=False, type=int, help="Random seed")

    arguments = parser.parse_args()

    # This is the code that will pass the tests, as the output does not contain a colon
    if not 0 < arguments.pctgc < 1:
        parser.error(f'--pctgc "{arguments.pctgc}" must be between 0 and 1')

    # If the program requires the seed, the tests won't pass, so see if it is set here.
    if arguments.seed is not None:
        random.seed(arguments.seed)

    try:
        out = open(arguments.outfile, 'wt', encoding='UTF-8') \
            if arguments.outfile else sys.stdout
    except FileExistsError:
        print(f'File already exists: {arguments.outfile}')
        sys.exit(-1)

    synth = Synthetic(arguments.outfile,
                      arguments.seqtype,
                      arguments.numseqs,
                      arguments.minlen,
                      arguments.maxlen,
                      arguments.pctgc)

    if synth.write():
        print(f'Done, wrote {arguments.numseqs} {arguments.seqtype.upper()} sequences to "{arguments.outfile}".')

    sys.exit(0)

