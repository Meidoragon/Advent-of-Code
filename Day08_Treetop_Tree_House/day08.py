#!/usr/bin/env python3
"""
Author : Meidoragon<Meidoragon@localhost> 
Date   : 2023-05-09
Purpose: solve day 8 of advent of code 2022.
Important to note that this would likely be faster by properly using a numpy
array, but I just wish to get it working right now. I can optimize later if I 
ever decide to come back to this.
"""

TEST_INPUT = """30373
25512
65332
33549
35390"""
PARSED_INPUT = [[3, 0, 3, 7, 3],
                [2, 5, 5, 1, 2],
                [6, 5, 3, 3, 2],
                [3, 3, 5, 4, 9],
                [3, 5, 3, 9, 0]]

import argparse
import os
import pprint as p
# ----------------------------------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Row, row, fight the power.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('intext',
                        nargs='?',
                        metavar='str',
                        help='Input. Accepts files.',
                        default=TEST_INPUT)
                        
    args = parser.parse_args()
    
    if args.intext != TEST_INPUT and os.path.isfile(args.intext):
        file = args.intext
        with open(file) as f:
            args.intext = f.read()
    return args
# ----------------------------------------------------------------------------
def parse_input(into) -> list[list[int]]:
    '''parses raw string input and maps to 2d array'''
    parse = []
    for ea in into.split('\n'):
        x = []
        for y in ea:
            x.append(int(y))
        parse.append(x)
    return parse
# ----------------------------------------------------------------------------

def isHidden(y, x, matrix = PARSED_INPUT) -> bool:
    '''returns boolean value for whether coordinate contains visible tree'''
    #this is going to be a mess. fix it later if we come back to this.
    isEdge = (y == 0 or y == len(matrix) or x == 0 or x == len(matrix[y]))
    if isEdge:
        return False
    value = matrix[y][x]
    vertical = getVertical(x, matrix)
    horizontal = matrix[y]
    if not lineHidden(x, value, horizontal):
        return False
    if not lineHidden(y, value, vertical):
        return False
    return True
    
    #print(f'hor: {horizontal}', f'vert: {vertical}', f'y: {y}', f'x: {x}', sep='\n')
    #visibility = []
# ----------------------------------------------------------------------------
def lineHidden(base, val, line) -> bool:
    plusHidden = False
    minusHidden = False
    for var in range(0, len(line), 1):
        if var == base:
            continue
        comp = line[var]
        if val <= comp:
            if var < base:
                minusHidden = True
            if var > base:
                plusHidden = True
    if plusHidden and minusHidden:
        return True
    else:
        return False
# ----------------------------------------------------------------------------
def getVertical(x, matrix = PARSED_INPUT):      #include default value for testing. probably unnecessary and bad practice
    retList = []
    for loopVar in matrix:
        retList.append(loopVar[x])
    return retList
# ----------------------------------------------------------------------------
def solve(matrix) -> int:
    height, width = len(matrix), len(matrix[0])
    visible = 0
    for yCoord, xCoord in xyGenerator(height, width):
        if not isHidden(yCoord, xCoord, matrix):
            visible += 1
    return visible
# ----------------------------------------------------------------------------
def xyGenerator(height, width):
    for a in range(0, width, 1):
        for b in range(0, height, 1):
            yield a, b
# ----------------------------------------------------------------------------
def test_parse_input():
    assert parse_input(TEST_INPUT) == PARSED_INPUT
# ----------------------------------------------------------------------------
def test_getVertical():
    x0 = [3, 2, 6, 3, 3]
    x1 = [0, 5, 5, 3, 5]
    x2 = [3, 5, 3, 5, 3]
    x3 = [7, 1, 3, 4, 9]
    x4 = [3, 2, 2, 9, 0]
    assert getVertical(0) == x0
    assert getVertical(1) == x1
    assert getVertical(2) == x2
    assert getVertical(3) == x3
    assert getVertical(4) == x4
# ----------------------------------------------------------------------------
def test_isHidden():
    assert not isHidden(1, 1) #top left five, should return false
    assert not isHidden(1, 2) #top middle five, should return false
    assert isHidden(1, 3)     #top right 1, should return true
    assert not isHidden(2, 1) #middle left 5, should return false
    assert isHidden(2, 2)     #center 3, should return true
    assert not isHidden(2, 3) #middle right, should return false
    assert isHidden(3, 1)     #bottom left, should return true
    assert not isHidden(3, 2) #bottom middle, should return false
    assert isHidden(3, 3)     #bottom right, should return true
    assert not isHidden(0, 3) #these next four are on the outside
    assert not isHidden(4, 3) #they should all return false
    assert not isHidden(3, 0)
    assert not isHidden(3, 4)
# ----------------------------------------------------------------------------
def test_solve():
    assert solve(PARSED_INPUT) == 21
# ----------------------------------------------------------------------------
def main():
    """Okay 3, 2, 1, Let's Jam"""
    args = get_args()
    print(solve(parse_input(args.intext)))
    
# ----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
