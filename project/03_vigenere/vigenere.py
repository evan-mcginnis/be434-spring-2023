#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-04-25
Purpose: Encryption
"""
import sys
import argparse


class Text:
    """
    Text file
    """
    def __init__(self, file: str, keyword: str):
        """
        Text file for encrypt/decrypt
        :param file: Name of file to read
        :param keyword: Cipher string
        """
        self._file = file
        self._shift = 0
        self._target = []
        self._only_alpha = []
        self._encrypted = []
        self._decrypted = []
        self._cleartext = []
        self._expanded = []

        self._alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._cipher = []
        self._keyword = keyword

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

        for i in range(len(self._only_alpha)):
            line = self._only_alpha[i]
            decrypted_line = []
            # The key is over only the current line, not the entire cleartext
            key = self.form_cipher(line)

            i = 0
            for char in line:
                if char in self._alpha:
                    encrypted_index = self._alpha.index(char)
                    key_index = self._alpha.index(key[i])
                    if (encrypted_index - key_index) >= 0:
                        decrypted_line.append(self._alpha[encrypted_index - key_index])
                    else:
                        decrypted_line.append(self._alpha[(encrypted_index - key_index) + len(self._alpha)])
                else:
                    decrypted_line.append(char)
                i += 1
            self._decrypted.append(decrypted_line)

        self._expand()

        return self._expanded

    def form_cipher(self, clear: str) -> str:
        """
        Form the cipher across the cleartext
        :param clear:
        :return: Cipher string
        """
        i = -1
        key = ""
        for char in clear:
            if i == len(self._keyword) - 1:
                # Start over
                i = 0
            else:
                i += 1
            key += self._keyword[i]
        return key

    def _expand(self):
        """
        Expand the encrytped text out to include the non-alpha characters
        :return:
        """
        self._expanded = []
        i = 0
        for line in self._target:
            current = ""
            j = 0
            for char in line:
                if char not in self._alpha:
                    current += char
                else:
                    if len(self._encrypted) > 0:
                        current += self._encrypted[i][j]
                    else:
                        current += self._decrypted[i][j]
                    j += 1
            i += 1
            self._expanded.append(current)
        return

    def encrypt(self) -> []:
        """
        Encrypt the contents of the target
        :return: Encrypted contents, one string per list item
        """
        for i in range(len(self._only_alpha)):
            line = self._only_alpha[i]
            encrypted_line = []
            # Not clear if the cipher starts over at the beginning of the line
            # or extends across the entire cleartext, so I'll assume the
            # former to see if the tests pass
            key = self.form_cipher(line)
            j = 0
            for char in line:
                if char in self._alpha:
                    cleartext_index = self._alpha.index(char)
                    encrypted_index = self._alpha.index(key[j])
                    if (cleartext_index + encrypted_index) < len(self._alpha):
                        encrypted_line.append(
                            self._alpha[cleartext_index + encrypted_index])
                    else:
                        encrypted_line.append(self._alpha[(cleartext_index + encrypted_index) - len(
                            self._alpha)])
                else:
                    encrypted_line.append(char)
                j += 1
            self._encrypted.append(encrypted_line)

        self._expand()

        return self._expanded

    def read(self):
        """
        Read the input file
        """
        try:
            with open(self._file, "r", encoding='UTF-8') as file:
                self._target = file.readlines()
            # Upper-case the target
            for i in range(len(self._target)):
                self._target[i] = self._target[i].upper()

            i = 0
            self._only_alpha = [""] * len(self._target)
            for line in self._target:
                for char in line:
                    if char in self._alpha:
                        self._only_alpha[i] += char
                i += 1

        except FileNotFoundError:
            raise FileNotFoundError
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment Vigenere: Encode/Decode',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input', metavar='FILE', type=str)

    parser.add_argument('-d', '--decode',
                        required=False,
                        action="store_true",
                        help="Decode file")

    parser.add_argument('-k', '--keyword',
                        required=False,
                        type=str,
                        default="CIPHER",
                        help="Cipher string")

    parser.add_argument('-o', '--outfile',
                        required=False,
                        type=str,
                        default=sys.stdout,
                        help="Output file")

    arguments = parser.parse_args()

    target = Text(arguments.input, arguments.keyword)
    try:
        target.read()
    except FileNotFoundError:
        parser.print_usage()
        print(f"No such file or directory: '{arguments.input}'")
        sys.exit(2)

    if arguments.decode:
        _decrypted = target.decrypt()
        for _line in _decrypted:
            arguments.outfile.write(f"{_line}")
    else:
        _encrypted = target.encrypt()
        for _line in target._expanded:
            arguments.outfile.write(f"{_line}")

    sys.exit(0)
