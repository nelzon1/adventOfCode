from pathlib import Path
import re
pointRE = re.compile("(\\d+),(\\d+)")
SOURCE = (500,0)
EMPTY = '.'
'''
step function
    returns 1 when it moves and 0 when it doesnt or a -1 if it fell to abyss

read file
create map
draw line

add sand
    step until 0
        
IN THE GRID, Y IS FIRST, but aALL POINTS ARE x.Y
'''
def parseLine(strIn):
    points = [(int(x[0]), int(x[1])) for x in pointRE.findall(strIn)]
    return points
def drawLine(a, b, grid):
    #vertical:
    if a[0] == b[0]:
        for i in range(0, (a[1] - b[1]) + (1 if a[1] > b[1] else -1), (a[1] - b[1]) // abs(a[1] - b[1])):
            grid[b[1] + i][b[0]] = '#'
    # horizontal:
    else:
        if a[1] == b[1]:
            for i in range(0, (a[0] - b[0]) + (1 if a[0] > b[0] else -1), (a[0] - b[0]) // abs(a[0] - b[0])):
                grid[b[1]][b[0] + i] = '#'
def drawSource(grid):
    grid[SOURCE[1]][SOURCE[0]] = '+'

def moveSand(pos,grid):
    x = pos[0]
    y = pos[1]
    #check below
    if y == len(grid) - 1:  # abyss
        return -1
    if grid[y+1][x] == EMPTY:
        pos[1] += 1
        return 1
    #check DL
    if grid[y+1][x-1] == EMPTY:
        pos[0] -= 1  # x --
        pos[1] += 1  # y ++
        return 1
    #check DR
    if grid[y+1][x+1] == EMPTY:
        pos[0] += 1  # x ++
        pos[1] += 1  # y ++
        return 1
    #blocked
    if x == SOURCE[0] and y == SOURCE[1]:
        return -1
    grid[y][x] = 'o'
    return 0

def addSand(grid):
    pos = [SOURCE[0], SOURCE[1]]  # Initial position below source
    moveResult = 1
    while moveResult == 1:
        moveResult = moveSand(pos, grid)
    return bool(moveResult + 1)

if __name__ == '__main__':
    print('Running AOC Day 14')
    filename = Path.joinpath(Path.cwd(), 'input/Day14.txt')
    with open(filename, 'r') as file:
        puzzle = [parseLine(line) for line in file.readlines()]

    maxDepth = max([max([z[1] for z in x]) for x in puzzle])
    maxWidth = max([max([z[0] for z in x]) for x in puzzle])
    minWidth = min([min([z[0] for z in x]) for x in puzzle])
    print("Maximum Depth: ", maxDepth)
    print("Maximum Depth: ", maxWidth)
    Area = [[EMPTY for x in range(maxWidth * 2 + 1)] for y in range(maxDepth + 3)]
    drawSource(Area)
    for line in puzzle:
        for i in range(len(line) - 1):
            drawLine(line[i], line[i+1], Area)
    drawLine((0, maxDepth+2), (maxWidth * 2, maxDepth+2), Area)

    ViewArea = [''.join(line[minWidth:]) for line in Area]
    moveResult = 1
    count = 0
    while (moveResult):
        moveResult = addSand(Area)
        count += int(moveResult)
    count += 1 # last piece on top
    print(count, " pieces of sand added.")
    for line in Area:
        print(''.join(line[minWidth - (maxWidth - minWidth):maxWidth + (maxWidth - minWidth)]))