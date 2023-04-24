#!/usr/bin/env python3
"""
Author : Meidoragon <Meidoragon@localhost>
Date   : 2022-12-21
Purpose: Row, row, fight the power.
"""
#map file inputs to numbers based on choice
win = {'A': 1, 'X': 1, 'B': 2, 'Y':2, 'C': 3, 'Z': 3}
#map file inputs to numbers based on whether to throw
lose = {'X': 0, 'Y': 3, 'Z': 6}
import argparse
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
                        help='Input file')
    return parser.parse_args()
# ----------------------------------------------------------------------------
def detWinner(opp, pla):
    """determine victor in rps, with 1,2,3 corresponding to r,p,s"""
    if opp == pla:
        return 3
    elif opp == 3 and pla == 1:
        return 6
    elif opp == 1 and pla == 3:
        return 0
    elif opp < pla:
        return 6
    else:
        return 0
# ----------------------------------------------------------------------------
def detChoice(opp, pla):
    """determine choice player needs to make"""
    if (opp == 1 and pla == 0) or (opp == 2 and pla == 6) or (opp == 3 and pla == 3):
        return 3
    elif (opp == 1 and pla == 3) or (opp == 2 and pla == 0) or (opp == 3 and pla == 6):
        return 1    
    else:
        return 2
# ----------------------------------------------------------------------------
def test_detWinner():
    assert detWinner(1, 1) == 3
    assert detWinner(1, 2) == 6
    assert detWinner(1, 3) == 0
    assert detWinner(2, 1) == 0
    assert detWinner(2, 2) == 3
    assert detWinner(2, 3) == 6
    assert detWinner(3, 1) == 6
    assert detWinner(3, 2) == 0
    assert detWinner(3, 3) == 3
# ----------------------------------------------------------------------------
def test_detChoice():
    assert detChoice (1, 0) == 3
    assert detChoice (1, 3) == 1
    assert detChoice (1, 6) == 2
    assert detChoice (2, 0) == 1
    assert detChoice (2, 3) == 2
    assert detChoice (2, 6) == 3
    assert detChoice (3, 0) == 2
    assert detChoice (3, 3) == 3
    assert detChoice (3, 6) == 1
# ----------------------------------------------------------------------------
def main():
    """Okay 3, 2, 1, Let's Jam"""
    args = get_args()
    opp = []
    pla = []
    #res = []
    ind = 0
    score = 0
    for line in args.file:
        opp.append(win[line[0]])
        pla.append(lose[line[2]])
        #score += pla[ind] + detWinner(opp[ind], pla[ind])
        score += pla[ind] + detChoice(opp[ind], pla[ind])
        #res.append(detWinner(opp[ind], pla[ind]))
        ind += 1
        #print(detWinner())
    print(f'Points: {score}')
# ----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
