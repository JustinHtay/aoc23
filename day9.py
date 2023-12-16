import sys
import numpy as np
import copy

DIGITS = '0123456789'
CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def part_a(file_name):

    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]
       
        out = []
        for line in lines:
            nums = [int(x) for x in line.split()]
            n = 1 
            while not all([x == 0 for x in np.diff(nums, n=n)]):
                n += 1
            next_sum = 0 
            while n != 0:
                next_sum = next_sum + np.diff(nums, n=n)[-1]
                n -= 1
            out.append(next_sum + nums[-1])
        print(sum(out))
                




def part_b(file_name):
    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]
       
        out = []
        for line in lines:
            nums = [int(x) for x in line.split()]
            n = 1 
            while not all([x == 0 for x in np.diff(nums, n=n)]):
                n += 1
            next_sum = 0 
            while n != 0:
                next_sum = np.diff(nums, n=n)[0] - next_sum
                n -= 1
            out.append(nums[0] - next_sum)
        print(sum(out))


if __name__ == "__main__":
    file_name = sys.argv[1]
    if sys.argv[2] == 'a':
        part_a(file_name)
    else:
        part_b(file_name)
