from pathlib import Path
'''
create a copy matrix
from the start, put the value of stepping on each location on that, if it's possible or a 1000 if not
we are looking for the shortest path
move to the location with the lowest value and repeat
stop when we get to the E location

'''

class Tile:
    def __init__(self, height):
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


if __name__ == '__main__':
    print('Running AOC Day 12')
    filename = Path.joinpath(Path.cwd(), 'input/Day12.txt')
    puzzle = ''
    START = (20, 0)
    EXIT = (20, 45)
    with open(filename, 'r') as file:
        puzzle = [x.strip() for x in file.readlines()]
    gridX = len(puzzle)
    gridY = len(puzzle[0])
    Map = [[0 for y in range(gridY)] for x in range(gridX)]
    Values = [[0 for y in range(gridY)] for x in range(gridX)]
    for i in range(gridX):
        for j in range(gridY):
            Map[i][j] = Tile(puzzle[i][j])
    print('Puzzle loaded')

    finished = False
    cur = [START[0],START[1]]

    while (not finished):
        #if exit, break and end
        if cur[0] == EXIT[0] and cur[1] == EXIT[1]:
            break

        #check up
        try:
            diff = Map[cur[0] - 1][cur[1]].height - Map[cur[0]][cur[1]].height
            if diff <= 1:
                Values[cur[0] - 1][cur[1]] = Values[cur[0]][cur[1]] + 1
        except IndexError:
            print(IndexError)

        #check down

        #check left

        #check right

        #move

