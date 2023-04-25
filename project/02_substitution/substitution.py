#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-04-24
Purpose: Encryption
"""
import sys
import argparse
import random


class Text:
    """
    Text file
    """
    def __init__(self, file: str, seed: int):
        """
        Text file for encrypt/decrypt
        :param file: Name of file to read
        :param shift: Amount of shift
        """
        self._file = file
        self._shift = 0
        self._target = []
        self._encrypted = []
        self._cleartext = []

        self._alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        random.seed(seed)
        self._scrambled = ''.join(random.sample(self._alpha, len(self._alpha)))

    @property
    def cleartext(self) -> []:
        """
        The cleartext, one string per entry of list
        :return: []
        """
        return self._cleartext

    @property
    def encrypted(self) -> []:
        """
        Encrypted list
        :return:
        """
        return self._encrypted

    @property
    def decrypted(self) -> []:
        """
        Decryted list
        :return:
        """
        return self._cleartext

    def decrypt(self) -> []:
        """
        Decrypt the contents of the target
        :return: Decrypted contents, one string per list item
        """
        for line in self._target:
            decrypted_line = []
            for char in line:
                if char in self._alpha:
                    # The decrypted char is the in the position
                    # corresponding to its scrambled peer
                    decrypted = self._alpha[self._scrambled.index(char)]
                    decrypted_line.append(decrypted)
                else:
                    decrypted_line.append(char)
            self._cleartext.append(''.join(decrypted_line))
        return self._cleartext

    def encrypt(self) -> []:
        """
        Encrypt the contents of the target
        :return: Encrypted contents, one string per list item
        """
        for line in self._target:
            encrypted_line = []
            for char in line:
                if char in self._alpha:
                    # The encrypted char is in the position corresponding
                    # to the cleartext peer
                    encrypted = self._scrambled[self._alpha.index(char)]
                    encrypted_line.append(encrypted)
                else:
                    encrypted_line.append(char)
            self._encrypted.append(''.join(encrypted_line))
        return self._encrypted

    def read(self):
        """
        Read the input file
        """
        try:
            with open(self._file, "r", encoding='UTF-8') as file:
                self._target = file.read().splitlines()
            for i in range(len(self._target)):
                self._target[i] = self._target[i].upper()

        except FileNotFoundError:
            raise FileNotFoundError


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment Caesar: Encode',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input', metavar='FILE', type=str)

    parser.add_argument('-d', '--decode',
                        required=False,
                        action="store_true",
                        help="Decode file")

    parser.add_argument('-s', '--seed',
                        required=False,
                        type=int,
                        default=3,
                        help="Random seed")

    parser.add_argument('-o', '--output',
                        required=False,
                        type=str,
                        default=sys.stdout,
                        help="Output file")

    arguments = parser.parse_args()

    target = Text(arguments.input, arguments.seed)
    try:
        target.read()
    except FileNotFoundError:
        parser.print_usage()
        print(f"No such file or directory: '{arguments.input}'")
        sys.exit(2)

    if arguments.decode:
        _decrypted = target.decrypt()
        for _line in _decrypted:
            print(f"{_line}")
    else:
        _encrypted = target.encrypt()
        for _line in _encrypted:
            print(f"{_line}")

    sys.exit(0)
