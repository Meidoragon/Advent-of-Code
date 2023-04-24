#!/usr/bin/env python3
"""
Author : Meidoragon <Meidoragon@localhost>
Date   : 2022-12-20
Purpose: Solve day 1 of Advent of Code.
"""
import argparse
import sys
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Get the arguments.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='?',
                        #default='./Day1_p1_input',
                        default='./test_input',
                        type=argparse.FileType('rt'),
                        help='Input file')
    args = parser.parse_args()
    #return parser.parse_args()
    return args
# --------------------------------------------------
def findLargest(lin):
    curLarg = 0
    for ea in lin:
        if ea > curLarg:
            curLarg = ea
    return curLarg
# --------------------------------------------------
def test_findLargest():
    assert findLargest((1, 2, 3, 4, 5, 6)) == 6
    assert findLargest((5660, 1234, 9999, 1122, 5643, 17)) == 9999

# --------------------------------------------------
def findTopThree(lin):
    curOne, curTwo, curThr = 0, 0, 0
    for ea in lin:
        if ea > curOne:
            curThr = curTwo
            curTwo = curOne
            curOne = ea
        elif ea > curTwo:
            curThr = curTwo
            curTwo = ea
        elif ea > curThr:
            curThr = ea
    return [curOne, curTwo, curThr]
# --------------------------------------------------
def test_findTopThree():
    assert findTopThree((1, 2, 3, 4, 5, 6)) == [6, 5, 4]
    assert findTopThree((5660, 1234, 9999, 1122, 5643, 17)) == [
        9999, 5660, 5643]
# --------------------------------------------------
def main():
    """Okay 3, 2, 1, Let's Jam"""
    args = get_args()
    dwarf = [0]
    dwarfInd = 0
    for line in args.file:
        if line.strip() != '':
            dwarf[dwarfInd] += int(line.strip())
        else:
            dwarf.append(0)
            dwarfInd += 1
    dwarf = findTopThree(dwarf)
    print(f'{dwarf[0]} + {dwarf[1]} + {dwarf[2]} = {dwarf[0]+dwarf[1]+dwarf[2]}')
    #print(findLargest(dwarf), file=sys.stdout)
    #print(args.file, file=sys.stdout)
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
