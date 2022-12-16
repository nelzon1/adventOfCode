from pathlib import Path
from functools import cmp_to_key


DEBUG = False
'''
compare

if types are different:
    convert to lists
    
if types are list:
    if either are len == 0, it loses
    iterate over each one, calling the same function
    if tie, move onto next
    if get to end, see which list ehausted first
    
if types are int:
    return -1 = tie / 0 = lose / 1 = win
    
'''

def compare (a , b):
    if DEBUG:
        print('Compare ', a, ' vs ', b)
    aType = type(a)
    bType = type(b)
    if (aType != bType):
        if aType == type(1):
            a = [a]
        else:
            b = [b]
        return compare(a,b)

    if (aType == type(list())):
        if len(a) == 0 and len(b) == 0:
            return -1
        if len(a) == 0 or len(b) == 0:
            if DEBUG:
                print('left is empty' if len(a)==0 else 'right is empty')
            return int( len(a) == 0 or not len(b) == 0 )
        for pair in zip(a,b):
            result = compare(pair[0],pair[1])
            if result != -1:
                return result
        if len(a) != len(b):
            if DEBUG:
                print('Ran out of items: ', 'left is smaller.' if len(a) < len(b) else 'right is smaller.')
            return int( len(a) < len(b) )
        else:
            return -1

    #type = int
    else:
        if a == b:
            return -1
        else:
            if DEBUG:
                print("Left is smaller" if a < b else "Right is smaller")
            return a < b

'''
Rewrite to be compliant with python comparator function.
'''
def compare2 (a , b):
    if DEBUG:
        print('Compare ', a, ' vs ', b)
    aType = type(a)
    bType = type(b)
    if (aType != bType):
        if aType == type(1):
            a = [a]
        else:
            b = [b]
        return compare2(a,b)

    if (aType == type(list())):
        if len(a) == 0 and len(b) == 0:
            return 0
        if len(a) == 0 or len(b) == 0:
            if DEBUG:
                print('left is empty' if len(a)==0 else 'right is empty')
            return -1 if len(a) == 0 else 1
        for pair in zip(a,b):
            result = compare2(pair[0],pair[1])
            if result != 0:
                return result
        if len(a) != len(b):
            if DEBUG:
                print('Ran out of items: ', 'left is smaller.' if len(a) < len(b) else 'right is smaller.')
            return -1 if len(a) < len(b) else 1
        else:
            return 0

    #type = int
    else:
        if a == b:
            return 0
        else:
            if DEBUG:
                print("Left is smaller" if a < b else "Right is smaller")
            return -1 if a < b else 1


if __name__ == '__main__':
    print('Running AOC Day 13')
    filename = Path.joinpath(Path.cwd(), 'input/Day13.txt')
    pairs = []
    with open(filename, 'r') as file:
        puzzle = [ x.strip() for x in file.readlines() if len(x.strip()) > 0]
        pairs = [puzzle[x:x+2] for x in range(0,len(puzzle),2)]

    dividerPackets = ["[[2]]", "[[6]]"]
    puzzle += dividerPackets
    for i in range(len(puzzle)):
        exec("puzzle[i] = " + puzzle[i])
    sortedPackets = sorted(puzzle,key=cmp_to_key(compare2))
    index1 = sortedPackets.index([[2]]) + 1
    index2 = sortedPackets.index([[6]]) + 1
    print("Index 1: ", index1, " Index 2: ", index2, " Product: ", index1 * index2)

    pairIndex = 1
    grandSum = 0
    for pair in pairs:
        exec("left = " + pair[0])
        exec("right = " + pair[1])
        inOrder = compare2(left, right)
        if DEBUG:
            print("Correct order for Pair", pairIndex, ": ", inOrder)
        grandSum += pairIndex if inOrder == -1 else 0
        pairIndex += 1

    print("Sum of in-order indexes: ", grandSum)