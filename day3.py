import sys
import numpy as np
import copy

DIGITS = '0123456789'

def part_a(file_name):

    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]
       
        LEN_LINE = len(lines[0])
        # pad the lines so we don't run into indexing errors
        pad_line = ''.join(['.' for x in range(LEN_LINE)])
        lines.insert(0, copy.deepcopy(pad_line))
        lines.append(pad_line)
        lines = ['.' + x + '.' for x in lines]
        
        
        LEN_LINE = len(lines[0])
        N_LINES = len(lines)
        
        out = 0
        for line_idx in range(N_LINES):
            nums = []
            line = lines[line_idx]
            parts = line.split('.')
            parts = list(set(parts))
            for part in parts:
                if len(part) > 0 and all([x in DIGITS for x in part]):
                    # we need to find the surrounding characters and check for a symbol
                    idxs = findall('.' + part + '.', line)
                    for idx in idxs:
                        idx += 1
                        other_chars = lines[line_idx-1][idx-1:idx+len(part)+1] + lines[line_idx+1][idx-1:idx+len(part)+1]
                        count = 0
                        for my_char in other_chars:
                            if my_char not in (DIGITS + '.'):
                                count += 1
                        if count > 0:
                            nums.append(int(part))
                            out += int(part) 
                
                elif len(part) > 0 and any([x in DIGITS for x in part]):
                    # there clearly is something adjoining these numbers, so let's add them all
                    changed_part = ''.join([x if x in DIGITS else ';' for x in part])
                    changed_part = changed_part.split(';')
                    for tmp in changed_part:
                        if len(tmp) > 0:
                            out += int(tmp)
                            nums.append(int(tmp))
        print(out)

def part_b(file_name):

    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]
       
        LEN_LINE = len(lines[0])
        # pad the lines so we don't run into indexing errors
        pad_line = ''.join(['.' for x in range(LEN_LINE)])
        lines.insert(0, copy.deepcopy(pad_line))
        lines.append(pad_line)
        lines = ['.' + x + '.' for x in lines]
        
        
        LEN_LINE = len(lines[0])
        N_LINES = len(lines)
       
        num_list = [] # (number as a string, line_idx, col_idx)

        out = 0
        # find all the numbers
        for line_idx in range(N_LINES):
            nums = []
            line = lines[line_idx]
            parts = line.split('.')
            parts = list(set(parts))
            for part in parts:
                if len(part) > 0 and all([x in DIGITS for x in part]):
                    # we need to find the surrounding characters and check for a symbol
                    idxs = findall('.' + part + '.', line)
                    for idx in idxs:
                        idx += 1
                        other_chars = lines[line_idx-1][idx-1:idx+len(part)+1] + lines[line_idx+1][idx-1:idx+len(part)+1]
                        count = 0
                        for my_char in other_chars:
                            if my_char not in (DIGITS + '.'):
                                count += 1
                        if count > 0:
                            num_list.append((part, line_idx, idx))
                
                elif len(part) > 0 and any([x in DIGITS for x in part]):
                    # there clearly is something adjoining these numbers, so let's add them all
                    changed_part = ''.join([x if x in DIGITS else ';' for x in part])
                    changed_line = ''.join([x if x in (DIGITS + '.') else ';' for x in line])


                    changed_part = changed_part.split(';')
                    assert(len(changed_part) == 2)
                    part_lens = [len(x) > 0 for x in changed_part]
                    if all(part_lens):
                        search_strs = ['.' + changed_part[0] + ';', ';' + changed_part[1] + '.']
                    elif part_lens[0] > 0:
                        search_strs = ['.' + changed_part[0] + ';']
                    elif part_lens[1] > 0:
                        search_strs = [';' + changed_part[1] + '.']

                    for substr in search_strs:
                        idxs = findall(substr, changed_line)
                        for idx in idxs:
                            num_list.append((substr[1:-1], line_idx, idx+1))

        # now we iterate thru the '*' characters
        for line_idx in range(N_LINES):
            line = lines[line_idx]
            star_idxs = findall('*', line)
            for idx in star_idxs:
                adj_nums = []
                for num in num_list:
                    if line_idx <= num[1] + 1 and line_idx >= num[1] - 1: # row-wise adjacent to this particular *
                        if idx >= num[2] - 1 and idx <= num[2] + len(num[0]): # col-wise adjacent
                            adj_nums.append(int(num[0])) 
                if len(adj_nums) == 2:
                    out += np.prod(adj_nums)

        print(out)



def findall(pattern, string):
    out = []
    i = string.find(pattern)
    while i != -1:
        out.append(i)
        i = string.find(pattern, i+1)
    return out


if __name__ == "__main__":
    file_name = sys.argv[1]
    if sys.argv[2] == 'a':
        part_a(file_name)
    else:
        part_b(file_name)
