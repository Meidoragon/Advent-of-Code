#!/usr/bin/env python3
"""
Author : Meidoragon<Meidoragon@localhost> 
Date   : 2023-05-01
Purpose: Row, row, fight the power.
"""
test_inputs = ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 
               'bvwbjplbgvbhsrlpgdmjqwftvncz', 
               'nppdvjthqldpwncqszvftbrmjlhg',
               'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
               'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
p1_answers = (7, 5, 6, 10, 11)
p2_answers = (19, 23, 23, 29, 26)

import argparse
import os
from collections import deque
# ----------------------------------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Row, row, fight the power.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input',
                        nargs='?',
                        metavar='str',
                        help='Input. Accepts files.',
                        default=test_inputs[0])
                        
    args = parser.parse_args()
    
    if args.input != test_inputs[0] and os.path.isfile(args.input):
        file = args.input
        with open(file) as f:
            args.input = f.read()
    return args
# ----------------------------------------------------------------------------
def main():
    """Okay 3, 2, 1, Let's Jam"""
    args = get_args()
    print(p1_solve(args.input))
    print(p2_solve(args.input))
    #test_p2_solve()

# ----------------------------------------------------------------------------
def p1_solve(input):
    indeck = deque(input)
    deck = deque([], 4)
    i = 0
    while len(set(deck)) != 4:
        deck.append(indeck.popleft())
        i +=1
    return i
# ----------------------------------------------------------------------------
def p2_solve(input):
    """hey why is this basically the same as p1 lmao"""
    indeck = deque(input)
    deck = deque([], 14)
    i = 0
    while len(set(deck)) != 14:
        deck.append(indeck.popleft())
        i +=1
    return i

# ----------------------------------------------------------------------------
def test_p1_solve():
    loopvar = 0
    while loopvar < len(test_inputs):
        assert p1_solve(test_inputs[loopvar]) == p1_answers[loopvar]
        loopvar += 1

# ----------------------------------------------------------------------------
def test_p2_solve():
    loopvar = 0
    while loopvar < len(test_inputs):
        assert p2_solve(test_inputs[loopvar]) == p2_answers[loopvar]
        loopvar += 1

# ----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
