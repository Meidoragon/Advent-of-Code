#!/usr/bin/env python3
"""
Author : Meidoragon<Meidoragon@localhost> 
Date   : 2023-01-11
Purpose: Row, row, fight the power.
"""
import argparse
import re
# ----------------------------------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Row, row, fight the power.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('file',
                        metavar='FILE',
                        nargs='?',
                        default='Y://code_projects/advent-of-code/Day04_Camp_Cleanup/Day4_input',
                        type=argparse.FileType('rt'),
                        help='A positional argument')
    return parser.parse_args()

# ----------------------------------------------------------------------------
def inpParse(assignment):
    s = re.findall(r'([0-9]+)', assignment)
    dorf1 = [int(s[0]), int(s[1])]
    dorf2 = [int(s[2]), int(s[3])]
    return dorf1,dorf2
# ----------------------------------------------------------------------------
def assCheck(assignment):

    dorf1, dorf2 = inpParse(assignment)

    if (dorf1[0] <= dorf2[0]) & (dorf1[-1] >= dorf2[-1]):
        ass = True
    elif (dorf2[0] <= dorf1[0]) & (dorf2[-1] >= dorf1[-1]):
        ass = True
    else:
        ass = False
    #print(f'{assignment} \n {ce}')
    return(ass)
# ----------------------------------------------------------------------------
def overlapCheck(assignment):
    dorf1, dorf2 = inpParse(assignment)

    if (dorf1[0] >= dorf2[0]) & (dorf1[0] <= dorf2[1]):
        return True
    elif (dorf2[0] >= dorf1[0]) & (dorf2[0] <= dorf1[1]):
        return True
    elif (dorf1[1] <= dorf2[1]) & (dorf1[1] >= dorf2[0]):
        return True
    elif (dorf2[1] <= dorf1[1]) & (dorf2[1] >= dorf1[0]):
        return True
    else:
        return False

# ----------------------------------------------------------------------------
def test_assCheck():
    assert assCheck('3-6,7-9') == False
    assert assCheck('55-56,54-59') == True
    assert assCheck('3-7,4-5') == True
    assert assCheck('4-5,5-7') == False
# ----------------------------------------------------------------------------
def test_overlapCheck():
    assert overlapCheck('3-6,7-9') == False
    assert overlapCheck('55-56,54-59') == True
    assert overlapCheck('3-7,4-5') == True
    assert overlapCheck('4-5,5-7') == True
    assert overlapCheck('2-4,6-8') == False
    assert overlapCheck('2-3,4-5') == False
    assert overlapCheck('5-7,7-9') == True
    assert overlapCheck('2-8,3-7') == True
    assert overlapCheck('6-6,4-6') == True
    assert overlapCheck('2-6,4-8') == True
    assert overlapCheck('19-86,13-18') == False
# ----------------------------------------------------------------------------
def main():
    """Okay 3, 2, 1, Let's Jam"""
    args = get_args()
    assval = 0
    ovlval = 0
    for line in args.file:
        if assCheck(line.rstrip()):
            assval += 1
        if overlapCheck(line.rstrip()):
            print(line.rstrip())
            ovlval += 1
    print(f'assval: {assval}')
    print(f'ovlval: {ovlval}')
    

# ----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
