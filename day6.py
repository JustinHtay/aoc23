import sys
import numpy as np
import copy

DIGITS = '0123456789'

def part_a(file_name):

    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]

        line_vec = []
        for line in lines:
            line_vec.append([x for x in line.split(' ') if len(x) > 0])

        
        out = []
        for race_idx in range(len(line_vec[0])):
            if race_idx > 0:
                dur = int(line_vec[0][race_idx])
                dist = int(line_vec[1][race_idx])
                tmp = []
                for time_held in range(dur):
                    if (dur - time_held) * time_held >= dist:
                        tmp.append(time_held)
                out.append(len(tmp))

        print(np.prod(out))



def part_b(file_name):
    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]

        vec = []
        for line in lines:
            tmp = line.split(':')
            val = [x for x in tmp[1] if x in DIGITS]
            vec.append(int(''.join(val)))

        print(vec)
       
        dur = vec[0]
        dist = vec[1]
        tmp = []
        for time_held in range(dur):
            if (dur - time_held) * time_held >= dist:
                tmp.append(time_held)

        print(len(tmp))


if __name__ == "__main__":
    file_name = sys.argv[1]
    if sys.argv[2] == 'a':
        part_a(file_name)
    else:
        part_b(file_name)
