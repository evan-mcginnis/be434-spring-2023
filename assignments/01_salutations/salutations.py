#!/usr/bin/env python3
"""
Author : evan <evanmc@yahoo.com>
Date   : 2023-01-25
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Assignment 1: print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='The greeting',
                        metavar='str',
                        type=str,
                        required=False,
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='Whom to greet',
                        metavar='str',
                        type=str,
                        required=False,
                        default='Stranger')

    parser.add_argument('-e',
                        '--excited',
                        help='Include an exclamation point',
                        required=False,
                        default=False,
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """
    Greeting main program
    """
    args = get_args()
    print(f"{args.greeting}, {args.name}{'!' if args.excited else '.'}")


# --------------------------------------------------
if __name__ == '__main__':
    main()
