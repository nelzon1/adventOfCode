from pathlib import Path
import re

if __name__ == '__main__':
    print('Running AOC Day 15')
    filename = Path.joinpath(Path.cwd(), 'input/Day15.txt')
    MAXINDEX = 4000000  # 4000000 Puzzle  20 Test
    with open(filename, 'r') as file:
        coords = [ [int(z) for z in re.compile('(-?\\d+)').findall(line)] for line in file.readlines() ]
    #create a list of sensor coords and their excluded "distance"
    sensors = [[x[0], x[1], abs(x[0] - x[2]) + abs(x[1] - x[3])] for x in coords]
    curPos = 0
    # loop over row 0 to 4000000
    solved = False
    for row in range(0, MAXINDEX + 1):
        # in each row, loop over each sensor
        # if it reaches, add to candidates & order candidates by left-most index
        touchingSensors = [[x[0], x[1], x[0] - (x[2] - abs(x[1] - row)), x[2] - abs(x[1] - row) ] for x in sensors if abs(x[1] - row) <= x[2]]
        touchingSensors.sort(key=lambda x: x[2])
        # loop through candidates, if there is a gap, stop and report it
        # start at x = 0
        curPos = 0
        for sens in touchingSensors:
            # if there is a gap of 1, this is the hole for our "beacon"
            if curPos == sens[2] - 2:
                solved = True
                break
            # update curPos with new sensor if it gets us further along the row
            curPos = sens[0] + sens[3] if sens[0] + sens[3] > curPos else curPos
        if solved:
            print('The x, y position is ', curPos + 1, row)
            print('The tuning frequency is: ', (curPos + 1) * 400000 + row)
            # put this in to keep searching in case my algorithm was wrong, it only finds 1 beacon
            solved = False
