#!/usr/bin/env python3
"""
Author : oom
Date   : 2020-06-07
Purpose: Emulate wc (word count)
"""

import argparse
import sys


# -----------------------------------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs="*",
                        type=argparse.FileType('r'),
                        default=[sys.stdin])

    return parser.parse_args()


# -----------------------------------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    files_arg = args.file

    total_lines = 0
    total_words = 0
    total_bytes = 0
    for file_arg in files_arg:
        num_lines = 0
        num_words = 0
        num_bytes = 0
        for line in file_arg:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)

        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes

        print("{:8}{:8}{:8} {}".format(
            num_lines, num_words, num_bytes, file_arg.name))

    if len(files_arg) > 1:
        print("{:8}{:8}{:8} {}".format(
            total_lines, total_words, total_bytes, "total"))


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
