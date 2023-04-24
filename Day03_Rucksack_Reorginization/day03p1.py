#!/usr/bin/env python3
"""
Author : Meidoragon<Meidoragon@localhost> 
Date   : 2023-01-08
Purpose: Solve Day 3 of Advent of Code 2022
"""
import argparse
import string

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
                        default='./Day03/test_input',
                        type=argparse.FileType('rt'),
                        help='Input file')
 
    return parser.parse_args()
# ----------------------------------------------------------------------------
def knapsack(firsec):
    first = set(firsec[:len(firsec)// 2])
    sec = set(firsec[len(firsec) // 2:])
    for ea in first:
        if ea in sec:
            return letters.index(ea) + 1
# ----------------------------------------------------------------------------
def main():
    """Okay 3, 2, 1, Let's Jam"""
    args = get_args()
    pointSum = 0
    for line in args.file:
        pointSum += knapsack(line)
    print(pointSum)

# ----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
