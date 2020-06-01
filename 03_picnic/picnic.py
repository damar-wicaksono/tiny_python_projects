#!/usr/bin/env python3
"""
Author : oom
Date   : 2020-06-01
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items (default: False)',
                        action='store_false')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items_arg = args.str
    flag_arg = args.sorted

    print("You are bringing {}.".format(items_arg))


# --------------------------------------------------
if __name__ == '__main__':
    main()
