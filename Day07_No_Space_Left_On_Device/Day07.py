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

MAX_SIZE = 10 ** 5  #100 thou

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
"""
consider writing code that would create a visual map of this nonsense just for fun
untill I do that, mapping children likely won't be used for anything. 
anything I could use it for is done by recursively adjusting directory size whenever I add a new file
"""
import argparse
import os
# ----------------------------------------------------------------------------
class filesys():
    """
    creates the file system object and has functions to add directories and files to it.
    automatically adds the root directory on __init__.
    """
    def __init__(self):
        self.group = {}
        self.userdir = self.add_new_direc('root', None)
        self.sysdir = self.userdir
    
    def cd(self, new_direc: object):
        self.userdir = new_direc

    def add_new_direc(self, name, parent):
        x = newdir(name, parent)
        self.group[name] = x
        return x
    
    def add_new_file(self, name: str, size: int):
        x = newfile(name, self.userdir, size)
        while self.sysdir.parent != None:
            self.sysdir.increase_size(size)
            self.sysdir = self.sysdir.parent
        self.sysdir = self.userdir
# ----------------------------------------------------------------------------
class newdir():
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self.size = 0
        self.children = []
        

    def add_child(self, child):
        self.children.append(child)
    
    def increase_size(self, inc: int):
        self.size += inc
    
# ----------------------------------------------------------------------------
class newfile():
    def __init__(self, name: str, parent: newdir, size: int):
        self.parent = parent
        self.size = size

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
def parse_line(line: str) -> int:
    """
    0: ignore this line
    1: add new dir
    2: add new file
    3: go up a level
    4: go down a level
    """
    if line[0] == '$':
        return parse_command(line)
    elif line[0:3] == 'dir': #probably this, might be line[0:2] depending on how slices work, I am not looking it up right now
        return 0
    elif line[0] in '0123456789':
        return 1
    else:
        raise Exception('parse line error with:', line)

# ----------------------------------------------------------------------------
def parse_command(line: str) -> int:
    pass
# ----------------------------------------------------------------------------
def build_map(inlist: list):
    for line in inlist:
        x = parse_line(line)
    return inlist
# ----------------------------------------------------------------------------
def main():
    """Okay 3, 2, 1, Let's Jam"""
    args = get_args()
    fs = build_map(args.intext.split('\n'))
    print(fs)

# ----------------------------------------------------------------------------
if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------
def test_parse_line():
    pass

# ----------------------------------------------------------------------------
def test_build_map():
    pass

# ----------------------------------------------------------------------------