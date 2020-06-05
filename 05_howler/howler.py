#!/usr/bin/env python3
"""
Author : oom
Date   : 2020-06-05
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# ----------------------------------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input string or a file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# ----------------------------------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.str
    outfile_arg = args.outfile

    if os.path.isfile(str_arg):
        str_arg = open(str_arg).read().rstrip()

    fh_out = open(outfile_arg, "wt") if outfile_arg else sys.stdout
    print(str_arg.upper(), file=fh_out, end="")


# ----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
