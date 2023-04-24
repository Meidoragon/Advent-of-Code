#!/usr/bin/env python3
"""tests for day2"""

import os
from subprocess import getstatusoutput, getoutput
prg1 = './day02.py'

# ----------------------------------------------------------------------------
def test_exists():
    """exists"""
    assert os.path.isfile(prg1)
# ----------------------------------------------------------------------------
def test_runnable():
    """Runs using python3"""

    out = getoutput(f"python3 {prg1}")
    assert out != ''

def test_executable():
    """Runs without invoking as an argument of python3"""
    out = getoutput(f"{prg1}")
    assert out != ''

def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg1} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')

def test_value():
    """test correctness and proper output"""

    rv, out = getstatusoutput(f'{prg1}')
    assert rv == 0
    #assert out == 'Points: 36'
    assert out == 'Points: 24'
    