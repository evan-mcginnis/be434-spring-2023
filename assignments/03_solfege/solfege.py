#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-02-11
Purpose: Decode the do-re-me song
"""

import argparse
import sys


class DoReMi:
    """
    DoReMi song responses
    """
    def __init__(self, theAssociations: {}):
        """
        DoReMi song responses
        :param: Associations dictionary
        """
        self._associations = theAssociations

    @property
    def associations(self) -> []:
        """
        The associations for the do-re-mi song
        :return:
        """
        return self._associations

    def association(self, theKey: str) -> str:
        """
        The associated phrase of the key
        :return: The phrase, or 'I don't know' if not found
        """
        phrase = ""
        try:
            phrase = f'{theKey}, {self._associations[theKey]}'
        except KeyError:
            phrase = f'I don\'t know "{theKey}"'
        return phrase


if __name__ == "__main__":

    associations = {"Do": "A deer, a female deer",
                    "Re": "A drop of golden sun",
                    "Mi": "A name I call myself",
                    "Fa": "A long long way to run",
                    "Sol": "A needle pulling thread",
                    "La": "A note to follow sol",
                    "Ti": "A drink with jam and bread"}

    parser = argparse.ArgumentParser(
        description='Assignment 3: Responses to the do-rm-mi sont',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('key', metavar='str', type=str, nargs='+', help="")

    arguments = parser.parse_args()

    do = DoReMi(associations)

    for key in arguments.key:
        print(do.association(key))

    sys.exit(0)
