#!/usr/bin/env python3
"""
Author : Meidoragon<Meidoragon@localhost> 
Date   : 2023-04-24
Purpose: Row, row, fight the power.
"""
#declarations
test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

"""
part two guess is that instead of moving one at a time,
P2 changes how many can be moved at once
probably the entire group, so they end up inverted from what the P1 movement would do
"""

"""
1. Take input, group by line.
2. separate the input groups by whether they are boxes or instructions.
3. change box grouping from lines in the instructions to stacks of boxes.
4. for each line of instruction, parse the instruction
5. use parsed instruction to operate the crane
"""

import argparse
import pprint as p
import re
reBoxes = re.compile(r" ([0-9]+( +[0-9]+)+) ")
# ----------------------------------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Row, row, fight the power.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("--input",
                        "-i",
                        metavar='input',
                        type=str,
                        help="input",
                        default=test_input)

    return parser.parse_args()

# ----------------------------------------------------------------------------
def main():
    """Okay 3, 2, 1, Let's Jam"""
    args = get_args()
    #print(args.input)
    #print()
    a = read_input(args.input)
    #p.pprint(a)
    #print()
    b = separate(a)
    #p.pprint(b['rows'])
    #print()
    #print(b['columns'])
    #print()
    #p.pprint(b['rows'])
    #print()
    #p.pprint(b['columns'])
    #print()
    #p.pprint(b['instructions'])
    c = tokenize(b['rows'], b['columns'])
    p.pprint(c)
    #print(c)
# ----------------------------------------------------------------------------
def read_input(y):
    return y.split('\n')

# ----------------------------------------------------------------------------
def separate(inlist):
    #print(inlist)
    rows = []
    instructions = []
    for line in inlist:
        #print(line)
        if line.rstrip() == '':
            continue
        elif '[' in line:
            rows.append(line)
        elif line[0:1] != 'm':
            colNum = line.split()[-1]
        else:
            instructions.append(line)
    return {'rows': rows, 'columns': int(colNum), 'instructions': instructions}

# ----------------------------------------------------------------------------
def tokenize(inlist, colNum):
    toklist = []
    for line in inlist:
        looper = 0
        linelist = []
        while looper < colNum:
            linelist.append(line[1 + looper * 4])
            looper += 1
        toklist.append(linelist[:])
    return toklist
# ----------------------------------------------------------------------------
def columns(intext):
    return intext

# ----------------------------------------------------------------------------
def movement(inlist, instructions):
    return inlist

# ----------------------------------------------------------------------------
def parse_instruct(line):
    return line

# ----------------------------------------------------------------------------
def solve(inlist):
    return inlist

# ----------------------------------------------------------------------------
def pOne(intext):
    return intext

# ----------------------------------------------------------------------------
def test_read_input():
    input_lines = ['    [D]    ',
                   '[N] [C]    ',
                   '[Z] [M] [P]',
                   ' 1   2   3 ',
                   '',
                   'move 1 from 2 to 1',
                   'move 3 from 1 to 3',
                   'move 2 from 2 to 1',
                   'move 1 from 1 to 2']
    assert read_input(test_input) == input_lines

# ----------------------------------------------------------------------------
def test_separate():
    input_lines = ['    [D]    ',
                   '[N] [C]    ',
                   '[Z] [M] [P]',
                   ' 1   2   3 ',
                   '',
                   'move 1 from 2 to 1',
                   'move 3 from 1 to 3',
                   'move 2 from 2 to 1',
                   'move 1 from 1 to 2']
    colNum = 3
    rows = ['    [D]    ',
            '[N] [C]    ',
            '[Z] [M] [P]']
    instructions = ['move 1 from 2 to 1',
                    'move 3 from 1 to 3',
                    'move 2 from 2 to 1',
                    'move 1 from 1 to 2']
    assert separate(input_lines) == {'rows': rows,
                                     'columns': colNum,
                                     'instructions': instructions}

# ----------------------------------------------------------------------------
def test_tokenize():
    rows = ['    [D]    ',
            '[N] [C]    ',
            '[Z] [M] [P]']
    toks = [[' ', 'D', ' '],
            ['N', 'C', ' '],
            ['Z', 'M', 'P']]
    assert tokenize(rows, 3) == toks
# ----------------------------------------------------------------------------
def test_columns():
    toks = [['', 'D', ''],
            ['N', 'C', ''],
            ['Z', 'M', 'P']]
    assert columns(toks) == [['Z', 'N'],
                             ['M', 'C', 'D'],
                             ['P']]

# ----------------------------------------------------------------------------
def test_movement():
    a = [['Z', 'N'],
         ['M', 'C', 'D'],
         ['P']]
    instruct = ['move 1 from 2 to 1',
                'move 3 from 1 to 3',
                'move 2 from 2 to 1',
                'move 1 from 1 to 2']
    b = [['C'],
         ['M'],
         ['P', 'D', 'N', 'Z']]
    assert movement(a, instruct) == b

# ----------------------------------------------------------------------------
def test_parse_instruct():
    case0 = 'move 1 from 2 to 1'
    case1 = 'move 3 from 1 to 3'
    case2 = 'move 2 from 2 to 1'
    case3 = 'move 1 from 1 to 2'
    
    assert parse_instruct(case0) == {'move': 1,
                                     'from': 2,
                                     'to': 1}
    assert parse_instruct(case1) == {'move': 3,
                                     'from': 1,
                                     'to': 3}
    assert parse_instruct(case2) == {'move': 2,
                                     'from': 2,
                                     'to': 1}
    assert parse_instruct(case3) == {'move': 1,
                                     'from': 1,
                                     'to': 2}

# ----------------------------------------------------------------------------
def test_solve():
    a = [['C'],
         ['M'],
         ['P', 'D', 'N', 'Z']]
    assert solve(a) == 'CMZ'

# ----------------------------------------------------------------------------
def test_pOne():
    assert pOne(test_input) == ('CMZ')

# ----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
