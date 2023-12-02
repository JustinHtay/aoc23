import sys
import numpy as np

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

DIGITS = '0123456789'

def part_a(file_name):

    game_settings = {
            'red': 12,
            'green': 13,
            'blue': 14
            }

    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]
        num = 0
        for line in lines:
            a = line.split(':')
            game_id = int(''.join([x for x in a[0] if x in DIGITS]))
            rounds = a[1].split(';')
            bad = False
            for rd in rounds:
                cols = rd.split(',')
                for col in cols:
                    for key in game_settings.keys():
                        if key in col:
                            num_withdrawn = int(''.join([x for x in col if x in DIGITS]))
                            print(num_withdrawn)
                            print(game_settings[key])
                            if num_withdrawn > game_settings[key]:
                                bad = True
            if not bad:
                num += game_id

        print(num)

def part_b(file_name):
    game_settings = {
            'red': 12,
            'green': 13,
            'blue': 14
            }

    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]
        num = 0
        for line in lines:

            store = {
                    'red': [],
                    'green': [],
                    'blue': []
                    }


            a = line.split(':')
            game_id = int(''.join([x for x in a[0] if x in DIGITS]))
            rounds = a[1].split(';')
            for rd in rounds:
                cols = rd.split(',')
                for col in cols:
                    for key in game_settings.keys():
                        if key in col:
                            num_withdrawn = int(''.join([x for x in col if x in DIGITS]))
                            store[key].append(num_withdrawn)
            num += np.prod([max(x) for x in store.values()])

        print(num)



if __name__ == "__main__":
    file_name = sys.argv[1]
    if sys.argv[2] == 'a':
        part_a(file_name)
    else:
        part_b(file_name)
