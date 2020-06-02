#!/usr/bin/env python3
"""
Author : oom
Date   : 2020-06-02
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input_text = args.arg

    print(f'str_arg = "{input_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
