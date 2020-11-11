""" Tests for grepper.py """

import os
import platform
import random
import string
from subprocess import getstatusoutput, getoutput

PRG = './grepper.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
PATTERNS = './tests/inputs/patterns.txt'
INPUT1 = './tests/inputs/input1.txt'
INPUT2 = './tests/inputs/input2.txt'


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.exists(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Prints usage with no args or for help """

    for arg in ['', '-h', '--help']:
        out = getoutput(f'{RUN} {arg}')
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_run1() -> None:
    """ Runs OK """

    out_file = 'out.txt'
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        cmd = f'{RUN} --pattern {PATTERNS} --file {INPUT1}'
        rv, out = getstatusoutput(cmd)
        assert rv == 0
        assert out == 'Done, wrote 3 matches to "out.txt."'
        assert os.path.isfile(out_file)

        contents = open(out_file).read().splitlines()
        assert contents == ['c foo', 'bar e', 'g baz h']

    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def test_run2() -> None:
    """ Runs OK """

    out_file = random_filename()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        cmd = f'{RUN} -p {PATTERNS} -f {INPUT1} {INPUT2} -o {out_file}'
        rv, out = getstatusoutput(cmd)
        assert rv == 0
        assert out == f'Done, wrote 6 matches to "{out_file}."'
        assert os.path.isfile(out_file)

        contents = open(out_file).read().splitlines()
        expected = [
            'c foo', 'bar e', 'g baz h',
            'do eiusmod tempor incididunt ut foo labore et dolore magna',
            'Duis aute irure dolor bar in reprehenderit in voluptate',
            'velit esse cillum dolore eu fugiat nulla pariatur baz.'
        ]
        assert contents == expected

    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def random_filename() -> str:
    """ Generate a random filename """

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
