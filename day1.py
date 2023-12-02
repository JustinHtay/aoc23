import sys
# (value, length)
mymap = { 'one': (1,3),
        'two': (2,3),
        'three': (3,5),
        'four': (4,4),
        'five': (5,4),
        'six': (6,3),
        'seven': (7, 5),
        'eight': (8, 5),
        'nine': (9,4)
        }


def part_a(file_name):
    with open(file_name, 'rb') as f:
        txt = f.read()
        lines = txt.split()
        num = 0
        for line in lines:
            vec = [int(x) for x in str(line) if x in '0123456789']
            num += 10 * vec[0] + vec[-1]
        print(num)


def part_b(file_name):
    with open(file_name, 'rb') as f:
        txt = f.read()
        lines = txt.split()
        num = 0
        for line in lines:
            vec = []
            line = str(line)
            og_len = len(line)
            line = line + 'zzzzzz'
            for ii in range(og_len):
                for key in mymap.keys():
                    if line[ii:ii+mymap[key][1]] == key:
                        vec.append(mymap[key][0])
                if line[ii] in '0123456789':
                    vec.append(int(line[ii]))
            print(vec)
            num += 10 * vec[0] + vec[-1]
        print(num)



if __name__ == "__main__":
    file_name = sys.argv[1]
    if sys.argv[2] == 'a':
        part_a(file_name)
    else:
        part_b(file_name)
