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
import pprint as p
# ----------------------------------------------------------------------------
class filesys():
    """
    creates the file system object and has functions to add directories and files to it.
    automatically adds the root directory on __init__.
    """
    def __init__(self, rootdir = 'root'):
        self.dirDict = {}
        self.fileDict = {}
        self.userdir = self.add_init_direc(rootdir)
        self.sysdir = self.userdir
    
    def cd(self, chDir = None):
        """new_direc defaults to self.userdir.parent"""
        if chDir == None:
            self.userdir = self.userdir.parent
        else:
            self.userdir = self.dirDict[chDir]
        self.sysdir = self.userdir

    def add_init_direc(self, name, parent = None):
        x = newdir(name, parent)
        self.dirDict[name] = x
        return x
    
    def add_new_direc(self, name, parent = None):
        if parent == None:
            parent = self.userdir
        x = newdir(name, parent)
        self.dirDict[name] = x
 
    
    def add_new_file(self, name: str, size: int):
        x = newfile(name, self.userdir, size)
        self.fileDict[name] = x
        
        #self.sysdir.increase_size(size)
        first_pass = True
        while (self.sysdir.parent != None or first_pass == True):
            first_pass = False 
            self.sysdir.increase_size(size)
            if self.sysdir.parent != None:
                self.sysdir = self.sysdir.parent
        self.sysdir = self.userdir
# ----------------------------------------------------------------------------
class newdir():
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self.size = 0
        
    def add_child(self, child):
        self.children.append(child)
    
    def increase_size(self, inc: int):
        self.size = self.size + inc
    
    def this(self):
        return{'name': self.name, 'parent': self.parent, 'size': self.size}
    
# ----------------------------------------------------------------------------
class newfile():
    def __init__(self, name: str, parent: newdir, size: int):
        self.parent = parent
        self.size = size
        self.name = name
    
    def this(self):
        return {'name': self.name, 'parent': self.parent, 'size': self.size}
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
    1: add new dir and cd in
    2: cd out
    3: add new file
    """
    if line == '$ ls':
        return 0
    elif line[0:3] == 'dir':
        return 0
    elif line == '$ cd /':
        return 4
    elif line == '$ cd ..':
        return 2
    elif line[0:4] == '$ cd':
        return 1
    elif line[0] in '0123456789':
        return 3
    else:
        raise Exception('parse line error with:', line)

# ----------------------------------------------------------------------------
def parse_command(line: str) -> int:
    pass
# ----------------------------------------------------------------------------
def build_map(inlist: list) -> filesys:
    #uses elifs because when I noticed that I would need to update python to use
    #some variety of switch statement I decided that I was too lazy to do that
    #just know that this would be a match...case section instead
    for line in inlist:
        lineParsed = parse_line(line)
        if lineParsed == 4:
            fs = filesys()
        elif lineParsed == 0:
            continue
        elif lineParsed == 1:
            #split line, send dir name to fs for new directory
            x = line.split()
            fs.add_new_direc(x[2])
            fs.cd(x[2])
        elif lineParsed == 2:
            fs.cd()
        elif lineParsed == 3:
            #split line, send filename and size to fs for new file
            x = line.split()
            fs.add_new_file(x[1], int(x[0]))
    return fs
# ----------------------------------------------------------------------------
def main():
    """Okay 3, 2, 1, Let's Jam"""
    args = get_args()
    fs = build_map(args.intext.split('\n'))
    for ea in fs.dirDict:
        print(ea, fs.dirDict[ea].size)
    print()
    for ea in fs.fileDict:
        print(ea, fs.fileDict[ea].size)


# ----------------------------------------------------------------------------
if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------
def test_parse_line():
    assert parse_line('$ ls') == 0              #just ls, ignore
    assert parse_line('$ cd /') == 4            #instantiate fs
    assert parse_line('1231516 q.mp3') == 3     #create file
    assert parse_line('$ cd ..') == 2           #move out
    assert parse_line('dir bjrbjh') == 0        #dir from ls, ignore because we only act on dir when cd
    assert parse_line('$ cd gjzdf') == 1        #change dir, create, and then move in

# ----------------------------------------------------------------------------
