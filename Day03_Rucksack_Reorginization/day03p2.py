#!/usr/bin/env python3
"""
Author : Meidoragon<Meidoragon@localhost> 
Date   : 2023-01-09
Purpose: Row, row, fight the power.
"""
import argparse
import string
import sys
letters = string.ascii_lowercase + string.ascii_uppercase

# ----------------------------------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Row, row, fight the power.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('file',
                        metavar='FILE',
                        nargs='?',
                        default='./test_input',
                        type=argparse.FileType('rt'),
                        help='A positional argument')
    args = parser.parse_args()
    sacks = []
    for line in args.file:
        sacks.append(line.strip())
    if len(sacks) % 3 != 0:
        parser.error('Input file must have a number lines evenly divisible by 3')
    return parser.parse_args()
# ----------------------------------------------------------------------------
def knapsack(dorfSack):
    check = []
    check2 = []
    for ea in dorfSack[0]:
        if ea in dorfSack[1] and ea in dorfSack[2]:
            return letters.index(ea) + 1  
# ----------------------------------------------------------------------------
def main():
    """Okay 3, 2, 1, Let's Jam"""
    args = get_args()
    knapSack = []
    dorfSack = []
    i = 0
    sackSum = 0
    for line in args.file:
        knapSack.append(line.strip())

    for ea in knapSack:
        dorfSack.append(set(ea))
        if i == 2:
            sackSum += knapsack(dorfSack)
            i = 0
            dorfSack = []
        else:
            i += 1
    print(sackSum)
# ----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
