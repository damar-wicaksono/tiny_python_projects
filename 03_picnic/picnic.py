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
                        nargs="+",
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
    items = args.str
    flag_arg = args.sorted
    
    if len(items) < 2:
        items_str = items[0]
    elif len(items) < 3:
        items_str = " and ".join(items)
    else:
        pass


    print("You are bringing {}.".format(items_str))


# --------------------------------------------------
if __name__ == '__main__':
    main()
