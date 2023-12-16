import sys
import numpy as np
import copy

CARDS = 'AKQJT98765432'
CARDS_B = 'AKQT98765432J'

def part_a(file_name):

    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]

        out = []
        for line in lines:
            tmp = line.split(' ')
            hand = tmp[0]
            bid = int(tmp[1])
            out.append((hand, bid))

        N = len(lines)
        # order the hands with good ol bubblesort
        for ii in range(N):
            for jj in range(N-1):
                str1 = determine_strength(out[jj][0])
                str2 = determine_strength(out[jj+1][0])
                winner = 0
                if str1 > str2:
                    winner = 1
                elif str2 > str1:
                    winner = 2
                else:
                    ct = 0
                    DONE = False
                    while ct < 5:
                        idx1 = CARDS.index(out[jj][0][ct])
                        idx2 = CARDS.index(out[jj+1][0][ct])
                        if idx1 < idx2:
                            winner = 1
                            break
                        elif idx1 > idx2:
                            winner = 2
                            break
                        else:
                            ct += 1

                if winner == 2:
                    tmp = copy.deepcopy(out[jj])
                    out[jj] = copy.deepcopy(out[jj+1])
                    out[jj+1] = copy.deepcopy(tmp)

        out.reverse() 
        tmp = 0
        for ii in range(N):
            tmp += (ii+1) * out[ii][1]
        
        print(tmp)



def part_b(file_name):

    with open(file_name, mode='r', encoding='utf-8') as f:
        txt = f.read()
        lines = [x for x in txt.split('\n')]

        out = []
        for line in lines:
            tmp = line.split(' ')
            hand = tmp[0]
            bid = int(tmp[1])
            out.append((hand, bid))

        N = len(lines)
        # order the hands with good ol bubblesort
        for ii in range(N):
            for jj in range(N-1):
                str1 = determine_strength_with_jokers(out[jj][0])
                str2 = determine_strength_with_jokers(out[jj+1][0])
                winner = 0
                if str1 > str2:
                    winner = 1
                elif str2 > str1:
                    winner = 2
                else:
                    ct = 0
                    DONE = False
                    while ct < 5:
                        idx1 = CARDS_B.index(out[jj][0][ct])
                        idx2 = CARDS_B.index(out[jj+1][0][ct])
                        if idx1 < idx2:
                            winner = 1
                            break
                        elif idx1 > idx2:
                            winner = 2
                            break
                        else:
                            ct += 1

                if winner == 2:
                    tmp = copy.deepcopy(out[jj])
                    out[jj] = copy.deepcopy(out[jj+1])
                    out[jj+1] = copy.deepcopy(tmp)

        out.reverse() 
        tmp = 0
        for ii in range(N):
            tmp += (ii+1) * out[ii][1]
        
        print(tmp)

# 7 is 5 of a kind, 6 is 4 of a kind, etc
def determine_strength(hand):
    hand_tmp = sorted(hand)

    vec = []
    for idx in range(5):
        ct = 0
        for x in hand_tmp:
            if x == hand_tmp[idx]:
                ct += 1
        vec.append(ct)

    ct = max(vec)

    if ct == 5: # 5 of a kind
        return 7
    elif ct == 4: # 4 of a kind
        return 6
    elif ct == 3:
        if any([x == 2 for x in vec]): # full house
            return 5
        else:
            return 4
    elif ct == 2:
        if sum([1 if x == 2 else 0 for x in vec]) == 4: # 2 pair
            return 3
        else: # 1 pair
            return 2

    elif ct == 1: # high card
        return 1

     
    assert(1 == 0)



# 7 is 5 of a kind, 6 is 4 of a kind, etc
def determine_strength_with_jokers(hand):
    hand_tmp = sorted(hand)

    if ''.join(hand_tmp) == 'JJJJJ': #silly edge case
        hand_tmp = ['A' for x in range(5)]

    # joker should simply be the most common element in list right
    no_joke = [x for x in hand_tmp if x != 'J']
    ele = max(set(no_joke), key=no_joke.count)
    hand_tmp = [ele if x == 'J' else x for x in hand_tmp]
    hand_tmp = ''.join(hand_tmp)


    vec = []
    for idx in range(5):
        ct = 0
        for x in hand_tmp:
            if x == hand_tmp[idx]:
                ct += 1
        vec.append(ct)

    ct = max(vec)

    if ct == 5: # 5 of a kind
        return 7
    elif ct == 4: # 4 of a kind
        return 6
    elif ct == 3:
        if any([x == 2 for x in vec]): # full house
            return 5
        else:
            return 4
    elif ct == 2:
        if sum([1 if x == 2 else 0 for x in vec]) == 4: # 2 pair
            return 3
        else: # 1 pair
            return 2

    elif ct == 1: # high card
        return 1

     
    assert(1 == 0)



if __name__ == "__main__":
    file_name = sys.argv[1]
    if sys.argv[2] == 'a':
        part_a(file_name)
    else:
        part_b(file_name)
