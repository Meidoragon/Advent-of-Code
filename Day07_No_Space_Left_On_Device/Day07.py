#!/usr/bin/env python3
"""
Author : Meidoragon<Meidoragon@localhost> 
Date   : 2023-05-01
Purpose: Row, row, fight the power.
"""
test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

test_answer = 95437

"""
Plan:
record each file and directory (probably as an object, though I could probably use a dict if I really can't figure out how I would go about that.)
include the parent and children of each directory and file as appropriate
 if file, then record size, and recursively adjust size of each ancestor
 if directory then .append that directory name to a list
once we've done that we can just iterate through that list (using object.dirname.size or something) and perform actions from there
"""
"""
a few basic snippets that would likely work, and I don't wish to forget them before I get started since I am delaying:
1 if line[0] == '$':
    parse_command()
  elif line[0:3] == 'dir': #probably this, might be line[0:2] depending on how slices work, I am not looking it up right now
    add_dir_to_obj()
  elif line[0] in '0123456789':
    add_file_to_obj()
  else:
    print('further testing necessary')  
"""

import argparse
import os
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
                        default=test_input)
                        
    args = parser.parse_args()
    
    if args.input != test_input and os.path.isfile(args.input):
        file = args.input
        with open(file) as f:
            args.input = f.read()
    return args
# ----------------------------------------------------------------------------
def main():
    """Okay 3, 2, 1, Let's Jam"""
    args = get_args()
    print(args.input)
# ----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
