import sys
import numpy as np
import copy
import multiprocessing

DIGITS = '0123456789'

def part_a(file_name):

    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]
        hdr = lines[0].split(':')
        start = []
        for part in hdr[1].split(' '):
            if len(part) > 0:
                start.append(int(part))

        maps_list = []
        in_map = False
        map_count = -1


        for line in lines[1:]:
            if len(line) > 0:
                if not in_map:
                    in_map = True
                    map_count += 1
                    maps_list.append([])
                else:
                    tmp = line.split(' ')
                    dest = int(tmp[0])
                    source = int(tmp[1])
                    length = int(tmp[2])
                    maps_list[map_count].append((dest, source, length))
            else:
                in_map = False


        final_locs = []
        for start_val in start:
            for my_map in maps_list:
                for fcn in my_map:
                    if start_val >= fcn[1] and start_val < fcn[1] + fcn[2]:
                        start_val = start_val - fcn[1] + fcn[0]
                        break
            final_locs.append(start_val)

        print(min(final_locs))


def part_b(file_name):
    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]
        hdr = lines[0].split(':')
        start = []
        for part in hdr[1].split(' '):
            if len(part) > 0:
                start.append(int(part))


        maps_list = []
        in_map = False
        map_count = -1


        for line in lines[1:]:
            if len(line) > 0:
                if not in_map:
                    in_map = True
                    map_count += 1
                    maps_list.append([])
                else:
                    # let's encode them in reverse - this will probably be faster
                    tmp = line.split(' ')
                    source = int(tmp[0])
                    dest = int(tmp[1])
                    length = int(tmp[2])
                    maps_list[map_count].append((dest, source, length))
            else:
                in_map = False
     

        end_points = []
        for ii in np.arange(0, len(start), 2):
            ii = int(ii)
            end_points.append(start[ii] + start[ii+1] - 1)

        END = max(end_points)
        # we're going to go thru the maps backwards
        maps_list.reverse()
        # brute force because I couldn't figure out some sort of bisection algorithm
        for start_point in range(0, END):
            start_val = start_point
            for my_map in maps_list:
                for fcn in my_map:
                    if start_val >= fcn[1] and start_val < fcn[1] + fcn[2]:
                        start_val = start_val - fcn[1] + fcn[0]
                        break
            success = False 
            success_val = 0
            for ii in np.arange(0, len(start), 2):
                if start_val >= start[ii] and start_val < start[ii] + start[ii+1]:
                    print(start_point)
                    return

            if start_point % 100000 == 0:
                print('done with ' + str(start_point))

        


if __name__ == "__main__":
    file_name = sys.argv[1]
    if sys.argv[2] == 'a':
        part_a(file_name)
    else:
        part_b(file_name)
