import sys
import numpy as np
import copy

DIGITS = '0123456789'

def part_a(file_name):

    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]
        
        out = 0
        for line in lines:
            count = 0
            line_vec = line.split(':')
            line_vec = line_vec[1].split('|')
            win_str = [x for x in line_vec[0].split(' ')]
            win_nums = []
            for tmp in win_str:
                if len(tmp) > 0:
                    win_nums.append(int(tmp))

            game_str = [x for x in line_vec[1].split(' ')]
            for tmp in game_str:
                if len(tmp) > 0 and int(tmp) in win_nums:
                    count += 1
            if count == 0:
                pass
            else:
                out += 2 ** (count - 1)

        print(out)

def part_b(file_name):
    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]
        card_store = [[0,1] for x in range(len(lines))] # (points, # occurances)
        
        out = 0
        for line_idx in range(len(lines)):
            line = lines[line_idx]
            count = 0
            line_vec = line.split(':')
            line_vec = line_vec[1].split('|')
            win_str = [x for x in line_vec[0].split(' ')]
            win_nums = []
            for tmp in win_str:
                if len(tmp) > 0:
                    win_nums.append(int(tmp))

            game_str = [x for x in line_vec[1].split(' ')]
            for tmp in game_str:
                if len(tmp) > 0 and int(tmp) in win_nums:
                    count += 1
   
            if count == 0:
                val = 0
            else:
                val = 2 ** (count-1)

            card_store[line_idx][0] = val
            for ii in range(count):
                card_store[ii + line_idx + 1][1] += card_store[line_idx][1]

        print(card_store)
        print(sum([x[1] for x in card_store]))


if __name__ == "__main__":
    file_name = sys.argv[1]
    if sys.argv[2] == 'a':
        part_a(file_name)
    else:
        part_b(file_name)
