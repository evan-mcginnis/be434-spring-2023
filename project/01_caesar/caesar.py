#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-04-24
Purpose: Encryption
"""
import sys
import argparse


class Text:
    """

    """
    def __init__(self, file: str, shift: int):
        """
        Text file for encrypt/decrypt
        :param file: Name of file to read
        :param shift: Amount of shift
        """
        self._file = file
        self._shift = shift
        self._target = []
        self._encrypted = []
        self._cleartext = []
        self._excluded = [" ", ",", ".", "'", "-", "—", "\n"]

    @property
    def cleartext(self) -> []:
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
                if char not in self._excluded:
                    under_a = (ord(char) - self._shift) - ord('A')
                    if under_a < 0:
                        base = ord('Z')
                        shift = abs(under_a + 1)
                    else:
                        base = ord(char)
                        shift = self._shift
                    decrypted_line.append(chr(base - shift))
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
                if char not in self._excluded:
                    over_z = (ord(char) + self._shift) - ord('Z')
                    if over_z > 0:
                        base = ord('A')
                        shift = over_z - 1
                    else:
                        base = ord(char)
                        shift = self._shift
                    encrypted_line.append(chr(base + shift))
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

    parser.add_argument('-n', '--number',
                        required=False,
                        type=int,
                        default=3,
                        help="Number of shifts")

    parser.add_argument('-o', '--outfile',
                        required=False,
                        type=str,
                        default=sys.stdout,
                        help="Output file")

    arguments = parser.parse_args()

    target = Text(arguments.input, arguments.number)
    try:
        target.read()
    except FileNotFoundError:
        parser.print_usage()
        print(f"No such file or directory: '{arguments.input}'")
        sys.exit(2)

    if arguments.decode:
        decrypted = target.decrypt()
        for line in decrypted:
            print(f"{line}")
    else:
        encrypted = target.encrypt()
        for line in encrypted:
            print(f"{line}")

    sys.exit(0)
