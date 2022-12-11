from pathlib import Path
import functools as ft
class Tree:
    def __init__(self, height, xpos, ypos):
        self.height = height
        self.x = xpos
        self.y = ypos
        self.visible = False
        self.score = 0

class Forest:

    def __init__(self, gridSize=3):
        self.grid = [[]*gridSize]*gridSize
        self.gridSize = gridSize

    def getHeight(self,x,y):
        return self.grid[x][y].height

    def loadForest(self,grid):
        if len(grid) < 2:
            raise Exception('bad grid')
        gridSize = len(grid)
        self.gridSize = gridSize
        self.grid = [[0] * gridSize for x in range(gridSize)]
        for i in range(gridSize):
            for j in range(gridSize):
                self.grid[j][i] = Tree(int(grid[i][j]), j, i)

    def isVisible(self, tree):
        x = tree.x
        y = tree.y
        visible = [True, True, True, True]
        #up
        for i in range(y ):
            if self.grid[x][y-i-1].height >= tree.height:
                visible[0] = False
                break
        #down
        for i in range(self.gridSize - y - 1):
            if self.grid[x][y+i+1].height >= tree.height:
                visible[1] = False
                break
        #left
        for i in range(x ):
            if self.grid[x-i-1][y].height >= tree.height:
                visible[2] = False
                break
        #right
        for i in range(self.gridSize - x  - 1):
            if self.grid[x+i+1][y].height >= tree.height:
                visible[3] = False
                break
        result = ft.reduce(lambda a, b: a or b, visible)
        tree.visible = result
        return result

    def determineVisibility(self):
        count = 0
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                count += int(self.isVisible(self.grid[i][j]))
        return count

    def scenicScore(self, tree):
        x = tree.x
        y = tree.y
        scores = [0, 0, 0, 0]
        #up
        for i in range(y ):
            scores[0] += 1
            if self.grid[x][y-i-1].height >= tree.height:
                break
        #down
        for i in range(self.gridSize - y - 1):
            scores[1] += 1
            if self.grid[x][y+i+1].height >= tree.height:
                break
        #left
        for i in range(x ):
            scores[2] += 1
            if self.grid[x-i-1][y].height >= tree.height:
                break
        #right
        for i in range(self.gridSize - x  - 1):
            scores[3] += 1
            if self.grid[x+i+1][y].height >= tree.height:
                break
        result = ft.reduce(lambda a, b: a * b, scores)
        tree.score = result
        return result

    def determineScores(self):
        maxScore = 0
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                tscore = int(self.scenicScore(self.grid[i][j]))
                if tscore > maxScore:
                    maxScore = tscore
        return maxScore

if __name__ == '__main__':
    print('Running AOC Day 8')
    filename = Path.joinpath(Path.cwd(), 'input/Day8.txt')
    forestInput = []
    with open(filename, 'r') as file:
        forestInput = file.readlines()
    forestInput = [x.strip() for x in forestInput]
    forest = Forest()
    forest.loadForest(forestInput)
    print('Input loaded.')
    #Part 1
    print('Number of visible trees: ', forest.determineVisibility())
    #Part 2
    print('Greatest Scenic Score: ', forest.determineScores())