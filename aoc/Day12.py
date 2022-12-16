from pathlib import Path
'''
create a copy matrix
create a vertex queue
from the start, put the value of stepping on each location on that, if it's possible or a 1000000 if not
add each vertex we touch to the queue and sort queue by lowest value for priority
we are looking for the shortest path
move to the location with the lowest value and repeat
stop when we get to the E location

have queue,
while we haven't visited our destination:
while queue full:
    take next item in queue
    update Tile's value from queue item
    add possible neighbours to queue with curVal + 1
    if curTile == 'E' then break
'''

class Tile:
    def __init__(self, height, x, y):
        self.orig = height
        if height == 'E':
            self.height = 26
            self.exit = True
            self.start = False
        elif height == 'S':
            self.height = 1
            self.start = True
            self.exit = False
        else:
            self.height = ord(height) - 96
            self.exit = False
            self.start = False
        self.visited = False
        self.x = x
        self.y = y
        self.value = 10**4

    def compareTile(self, b):
        return b.height - self.height <= 1 and b != self and b.value > self.value + 1
def step(tile, val, heightMap, parent):
    testTiles = []
    try:  # check up
        if tile.y > 0:
            testTiles.append( heightMap[tile.y-1][tile.x] )
    except IndexError:
        None
    try:  # check down
        testTiles.append( heightMap[tile.y + 1][tile.x])
    except IndexError:
        None
    try:  # check left
        if tile.x > 0:
            testTiles.append( heightMap[tile.y][tile.x - 1])
    except IndexError:
        None
    try:  # check right
        testTiles.append( heightMap[tile.y][tile.x + 1])
    except IndexError:
        None
    return [[x, tile.value+1, tile] for x in testTiles if tile.compareTile(x)]


if __name__ == '__main__':
    print('Running AOC Day 12')
    filename = Path.joinpath(Path.cwd(), 'input/Day12.txt')
    puzzle = ''
    START = (20, 0)
    STARTTEST = (0, 0)
    EXIT = (20, 45)
    EXITTEST = (2, 5)
    with open(filename, 'r') as file:
        puzzle = [x.strip() for x in file.readlines()]
    gridX = len(puzzle)
    gridY = len(puzzle[0])
    Map = [[0 for y in range(gridY)] for x in range(gridX)]
    Values = [[10**6 for y in range(gridY)] for x in range(gridX)]
    for i in range(gridX):
        for j in range(gridY):
            Map[i][j] = Tile(puzzle[i][j],j,i)
    print('Puzzle loaded')

    finished = False
    startValue = 0

    #priorityQueue = [ [Map[STARTTEST[0]][STARTTEST[1]], startValue, None] ]
    priorityQueue = [ [Map[START[0]][START[1]], startValue, None] ]

    while (len(priorityQueue) > 0):
        queueItem = priorityQueue.pop(0)
        tile = queueItem[0]
        if tile.visited and queueItem[1] >= Values[tile.y][tile.x]:
            continue
        tile.visited = True
        #update Value Map
        tile.value = queueItem[1] if queueItem[1] < tile.value else tile.value
        Values[tile.y][tile.x] = tile.value
        priorityQueue += step(tile, queueItem[1], Map, queueItem[2])
        priorityQueue.sort(key=lambda x: x[1])
        #if we're on the exit, stop and report back its total
        #if tile.exit:
        #    break

    #steps = Values[EXITTEST[0]][EXITTEST[1]]
    steps = Values[EXIT[0]][EXIT[1]]
    print("Optimal route found, it takes: ", steps, " steps.")
    print("Result:")
    # for row in Map:
    #     print(' '.join([x.orig for x in row]))
    # for row in Values:
    #     print(' '.join([f'{x:02}' for x in row]))

