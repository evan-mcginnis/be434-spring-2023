#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-02-04
Purpose: Sum numbers on command line
"""

import argparse
import sys


class Arithmatic:
    """
    Arithmatic operations on array of numbers
    """
    def __init__(self, numbers: [], operator: str):
        """

        :param numbers:
        :param operator:
        """
        self._numbers = numbers
        self._operator = operator

    @property
    def numbers(self) -> []:
        """
        The numbers for the current operation.
        :return:
        """
        return self._numbers

    def sum(self) -> float:
        """
        Sum the numbers
        :return:
        """
        return sum(self._numbers)

    @property
    def operator(self) -> str:
        """
        The current operator
        :return:
        """
        return self._operator

    def equation(self) -> str:
        """
        The string representation of the equation
        :return:
        """
        the_equation = ""
        elements = len(self._numbers)
        for number in self._numbers:
            elements -= 1
            the_equation += f'{str(number)} {self._operator + " " if elements else ""}'
        return the_equation


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment 2: sum numbers on command line',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbers', metavar='int', type=int, nargs='+', help="numbers")

    arguments = parser.parse_args()

    math = Arithmatic(arguments.numbers, '+')
    print(f'{math.equation()}= {math.sum()}')

    sys.exit(0)
