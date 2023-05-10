#!/usr/bin/env python3
"""
Author : Meidoragon<Meidoragon@localhost> 
Date   : 2023-05-09
Purpose: Row, row, fight the power.
"""

test_input = """30373
25512
65332
33549
35390"""

import argparse
import os
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
                        default=test_input)
                        
    args = parser.parse_args()
    
    if args.intext != test_input and os.path.isfile(args.intext):
        file = args.intext
        with open(file) as f:
            args.intext = f.read()
    return args

# ----------------------------------------------------------------------------
def main():
    """Okay 3, 2, 1, Let's Jam"""
    args = get_args()

# ----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
