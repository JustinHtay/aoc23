import sys
import numpy as np
import copy
from math import lcm

DIGITS = '0123456789'
CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def part_a(file_name):

    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]

        directions = lines[0]
        net_lines = lines[2:]

        net = {}
        for line in net_lines:
            tmp = line.split('=')
            name = tmp[0].strip()
            tmp = tmp[1].split(',')
            left = ''.join([x for x in tmp[0] if x in CHARS])
            right = ''.join([x for x in tmp[1] if x in CHARS])
            net[name] = {'L': left,
                    'R': right
                    }

        ptr = 'AAA'
        ct = 0
        idx = 0
        while ptr != 'ZZZ':
            ptr = net[ptr][directions[idx]]
            ct += 1
            idx = (idx + 1) % len(directions)


        print(ct)

        



def part_b(file_name):
    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]

        directions = lines[0]
        net_lines = lines[2:]

        starts = []

        net = {}
        for line in net_lines:
            tmp = line.split('=')
            name = tmp[0].strip()
            tmp = tmp[1].split(',')
            left = ''.join([x for x in tmp[0] if x in CHARS])
            right = ''.join([x for x in tmp[1] if x in CHARS])
            net[name] = {'L': left,
                    'R': right
                    }
            if name[2] == 'A':
                starts.append(name)

        print(starts)
        out = []
        for ptr in starts:
            ct = 0
            idx = 0
            while ptr[2] != 'Z':
                ptr = net[ptr][directions[idx]]
                ct += 1
                idx = (idx + 1) % len(directions)
            out.append(ct)


        print(lcm(*out))


if __name__ == "__main__":
    file_name = sys.argv[1]
    if sys.argv[2] == 'a':
        part_a(file_name)
    else:
        part_b(file_name)
