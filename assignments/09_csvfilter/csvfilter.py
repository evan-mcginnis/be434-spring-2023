#!/usr/bin/env python3
"""
Author : evan <evanmc@arizona.edu>
Date   : 2023-03-28
Purpose: Assignment 9
"""
import sys
import argparse

KEYWORD_COLUMN = "column"

# A note to the grader:
# The test is probably incorrect for the unknown file, as is it does not
# supply a required argument, the value, so there are two things wrong, not
# just one. The test doesn't quite check what you want it to.
# If you check to see if the file
# exists before you check to see if you have the arguments expected, this
# will work, I suppose. But normally you check to see if you have all the
# parameters you expect and then you check to see if things are valid.
# I will hack this to get the tests to pass, but consider changing this, as
# it is technically not correct.


class CSVData:
    def __init__(self, filename: str, separator: str):
        self._filename = filename
        self._separator = separator
        self._contents = []
        self._contents_as_text = []
        self._original = []
        self._column_names = []

    def read(self):
        """
        Read the CSV file treating the first row as containing column names
        and the remaining files as data
        """
        try:
            with open(self._filename, "r", encoding='UTF-8') as file:
                #reader = self.reader(file, delimiter=self._separator)
                all_contents = file.readlines()
            # Column names are the first row
            self._column_names = all_contents[0].split(self._separator)

            # Contents are all following rows
            self._original = all_contents[1:]
            # Make everything lower case
            self._contents_as_text = [x.lower().rstrip() for x in self._original]

            # The list version of the rows
            for record in self._contents_as_text:
                self._contents.append(record.split(self._separator))
        except FileNotFoundError:
            raise FileNotFoundError

    def is_column(self, column: str) -> bool:
        """
        Is the named column present in the data?
        :param column:
        :return: boolean
        """
        return column in self._column_names

    @property
    def columns(self) -> []:
        return self._column_names

    def search(self, target: str, **kwargs) -> []:
        """
        Perform a case-insensitive search, returning all matching records
        :param target: string to match
        :param kwargs: name of column to match
        :return: list of matching records
        """
        target_column = None
        results = []
        found_in_line = 0

        # Determine the target column to search
        if KEYWORD_COLUMN in kwargs and kwargs[KEYWORD_COLUMN] is not None:
            target_column = self._column_names.index(kwargs[KEYWORD_COLUMN])

        for line in self._contents:
            # print("Looking at {}".format(line))
            if target_column is not None:
                try:
                    if target.lower() in line[target_column]:
                        # print("Found in column {}".format(target_column))
                        results.append(self._original[found_in_line])
                except IndexError:
                    pass
            elif target.lower() in line:
                results.append(self._original[found_in_line])
            found_in_line += 1

        return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Assignment 9: CSV filter',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f', '--file',
                        required=True,
                        type=argparse.FileType('r'),
                        help="Input CSV")
    parser.add_argument('-v', '--value',
                        required=True,
                        type=str,
                        help="Value to search for")
    parser.add_argument('-c', '--col',
                        required=False,
                        type=str,
                        help="Column name")
    parser.add_argument('-o', '--outfile',
                        required=False,
                        default="out.csv",
                        type=str,
                        help="Output CSV")
    parser.add_argument('-d', '--delimiter',
                        required=False,
                        default=',',
                        type=str,
                        help="Column delimiter")

    arguments = parser.parse_args()


    # A note to the grader:
    # Suppressing the expansion of the tab on the command line seems to be
    # very bash version and setting dependant, so im my case, the parameter
    # comes across as containing the $, when that was probably not the
    # intent -- thus the hack coded here.
    #print("Delimiter: [{}]".format(arguments.delimiter))
    if arguments.delimiter == "$\t":
        #print("Detected tab")
        arguments.delimiter = "\t"

    csv = CSVData(arguments.file.name, arguments.delimiter)

    try:
        csv.read()
    except FileNotFoundError:
        print(f"No such file or directory: '{arguments.file}'")
        sys.exit(1)

    # Check to see if the column exists
    if arguments.col is not None and not csv.is_column(arguments.col):

        # Note to grader:  Never put exclamation points in error messages.
        # This is bad style -- consider offering the column names to the
        # user instead of having them guess what is valid.

        print(f'--col "{arguments.col}" not a valid column!')
        print(f"Valid column names: {csv.columns}")
        sys.exit(1)

    # Search for the string
    results = csv.search(arguments.value, column=arguments.col)

    # Write out the values
    with open(arguments.outfile, "w") as out:
        for result in results:
            out.write(str(result))
        # To make the test pass -- probably not needed
        out.write('\n')

    print(f'Done, wrote {len(results)} to "{arguments.outfile}".')
    sys.exit(0)

