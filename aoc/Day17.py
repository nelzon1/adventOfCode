from pathlib import Path
from itertools import cycle

SHAPES = {'A':[(0,0), (1,0), (2,0), (3,0)],
          'B':[(1,0),(0,1),(1,1),(2,1),(1,2)],
          'C':[(0,0),(1,0),(2,0),(2,1),(2,2)],
          'D':[(0,0),(0,1),(0,2),(0,3)],
          'E':[(0,0),(1,0),(0,1),(1,1)]}
shapes = [SHAPES.keys()]
def validateMove(newPos,shapeIndex, Map):
    if newPos[0] < 0 or newPos[1] == 0:
        return False
    valid = True
    for piece in SHAPES[shapeIndex]:
        try:
            if Map[newPos[0] + piece[0]][newPos[1] + piece[1]] != '.':
                return False
        except IndexError:
            return False
    return True

def saveMove(newPos, shapeIndex, Map):
    for piece in SHAPES[shapeIndex]:
        Map[newPos[0] + piece[0]][newPos[1] + piece[1]] = '#'
    return newPos[1] + max([x[1] for x in SHAPES[shapeIndex]])


if __name__ == '__main__':
    print('Running AOC Day 17')
    filename = Path.joinpath(Path.cwd(), 'input/Day17.txt')
    puzzle = ''
    with open(filename, 'r') as file:
        puzzle = file.readline().strip()
    shapeCycle = cycle(SHAPES.keys())
    moveCycle = cycle(puzzle)
    turboCycle = len(puzzle) * 5
    towerHeight = 0
    MAXBLOCKS = turboCycle * 10 # 2022
    MAXHEIGHT = MAXBLOCKS * 3
    Map = [['.' for i in range(MAXHEIGHT)] for j in range(7)]
    cycleTest = [0]

    blockCount = 0
    print("Starting")
    while blockCount < MAXBLOCKS:
        if blockCount % 1000000 == 0:
            print(blockCount, ' blocks dropped.')
        moveCount = 0
        #new block
        curShape = next(shapeCycle)
        curPos = [2, towerHeight + 4] #  start position of the bottom left block
        while True:
            moveCount += 1
            if moveCount % 2 == 1:
                dir = next(moveCycle)
                if dir == '<':
                    #left
                    curPos[0] = curPos[0] - 1 \
                        if curPos[0] > 0 and validateMove((curPos[0] - 1, curPos[1]),curShape, Map) \
                        else curPos[0]
                else:
                    #right
                    curPos[0] = curPos[0] + 1 \
                        if curPos[0] < 6 and validateMove((curPos[0] + 1, curPos[1]), curShape, Map) \
                        else curPos[0]
            else:
                #down
                if validateMove((curPos[0],curPos[1] - 1), curShape, Map):
                    curPos[1] = curPos[1] - 1
                else:
                    tHeight = saveMove((curPos[0],curPos[1]), curShape, Map)
                    towerHeight = tHeight if tHeight > towerHeight else towerHeight
                    cycleTest.append(towerHeight)
                    blockCount += 1
                    break

    for i in range(towerHeight, towerHeight - 15, -1):
        print('|', end='')
        for j in range(7):
            print(Map[j][i], end='')
        print('|')
    print('|||||||||')
    print('|||||||||')
    for i in range(15, 0, -1):
        print('|', end='')
        for j in range(7):
            print(Map[j][i], end='')
        print('|')
    print('+-------+')

    with open('Day17Data.csv','w') as file:
        for num in [str(x) for x in cycleTest]:
            file.write(num + '\n')
    print('Complete')
    print('Tower max height: ', towerHeight)
    print('turbocyle: ', turboCycle)