#!/usr/bin/env python3
"""
Author : oom
Date   : 2020-06-11
Purpose: Rock the Casbah
"""

import argparse


# ----------------------------------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar="letter",
                        nargs="+",
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=open('gashlycrumb.txt'))

    return parser.parse_args()


# ----------------------------------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    letters = args.letter
    fh = args.file

    # Create dictionary from file:
    gashlycrumb = dict()
    for line in fh:
        gashlycrumb[line[0].lower()] = line

    # Loop over letter and show the dict entry
    for letter in letters:
        if letter.lower() in gashlycrumb:
            print(gashlycrumb[letter.lower()], end="")
        else:
            print(f"I do not know \"{letter}\".")

# ----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
