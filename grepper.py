#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2020-11-11
Purpose: Find patterns in files
"""

import argparse
import re
from typing import List, NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    pattern_file: TextIO
    search_files: List[TextIO]
    out_file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Find patterns in files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-p',
                        '--pattern',
                        help='Patterns file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True,
                        nargs='+')

    parser.add_argument('-o',
                        '--out_file',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    args = parser.parse_args()

    return Args(pattern_file=args.pattern,
                search_files=args.file,
                out_file=args.out_file)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    patterns = list(map(lambda s: re.compile(s.rstrip()), args.pattern_file))
    num_found = 0

    for fh in args.search_files:
        for line in map(str.rstrip, fh):
            for regex in patterns:
                if regex.search(line):
                    num_found += 1
                    print(line, file=args.out_file)

    print(f'Done, wrote {num_found} matches to "{args.out_file.name}."')


# --------------------------------------------------
if __name__ == '__main__':
    main()
