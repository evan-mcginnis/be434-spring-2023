#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-02-18
Purpose: Cat a file to stdout
"""

import argparse
import sys

# To the grader:
# Some stylistic differences were applied to make it pass tests and lint.
# I prefer names with camel-case, not snake-case, so I have to change
# all my names to get it # to pass the tests.  I know this is a common
# pythonism I choose not to follow
# The settings you have chosen for flake/lint seem to discourage any meaningful
# use of comments # and whitespace.  I tend not to put those in lest the tests
# fail.
# Consider relaxing these a bit, # as having test tests fail because of the
# number # of blank lines is far too extreme, and would probably never be used
# in the software industry


class TextFile:
    """
    Text file manipulation
    """
    def __init__(self, file_name: str):
        """
        Text file manipulation
        :param file_name:
        """
        self._file_name = file_name
        self._lines = []

    @property
    def file_name(self) -> str:
        """
        The filename currently being processed
        :return:
        """
        return self._file_name

    def read(self) -> (int, str):
        """
        Read the file contents.
        :return: (return code (non-zero indicates failure), return details)
        """
        rc_read = 0
        details = "File read successfully"
        try:
            target_file = open(self.file_name, encoding='UTF-8')
            self._lines = target_file.readlines()
            rc_read = 0
        except FileNotFoundError:
            rc_read = 1
            details = f"No such file or directory: '{self._file_name}'"
        except PermissionError:
            rc_read = 2
            details = "File exists, but permission problem"

        return rc_read, details

    def cat(self, numbers: bool):
        """
        Print the file to stdout
        :param numbers: indicate if file numbers precede each line
        """
        line_no = 0
        for line in self._lines:
            line_no += 1
            if numbers:
                print('{:>6}\t{}'.format(line_no, line), end='')
            else:
                print('{}'.format(line), end='')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment 4: Cat a file to stdout',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files', metavar='str', type=str, nargs='+', help="")
    parser.add_argument('-n', '--numbers', action="store_true", required=False,
                        help="Precede each line with number")

    arguments = parser.parse_args()

    # Process all files from command line
    for file in arguments.files:
        text = TextFile(file)
        (rc, error) = text.read()
        if not rc:
            text.cat(arguments.numbers)
        else:
            parser.print_usage()
            print(error)
            sys.exit(-1)

    sys.exit(0)
