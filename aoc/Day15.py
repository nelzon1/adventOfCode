from pathlib import Path
import re
from ClusterShell import RangeSet

class Range:

    start = 0
    end = 0
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def overlaps(self, a):
        return a.start - 1 <= self.end and a.end + 1 >= self.start

    def merge(self, a):
        return [Range(min([self.start, a.start]), max([self.end, a.end]))] \
            if self.overlaps(a) \
            else sorted([self, a], key=lambda x: x.start)

    def intersect(self, a):
        return Range(max([self.start, a.start]), min([self.end, a.end])) if self.overlaps(a) else None

class RangeSet:

    ranges = []
    def init(self):
        self.ranges=[]

    def add(self,nRange):
        tlist = self.ranges[:]
        #self.ranges = []
        #merge with each range:
        merges = 0
        for i, z in enumerate(tlist):
            if nRange.overlaps(z):
                tlist = tlist[:i] + nRange.merge(z) + [x for x in reversed(tlist[-1:i:-1])]
                merges += 1
                break
        tlist += [nRange] if not merges else []
        self.ranges = []
        #re-merge all ranges
        curRange = tlist[0]
        tranges = [tlist[0]]
        for i in range(len(tlist) - 1):
            tranges = curRange.merge(tlist[i+1])
            curRange = tranges[-1]
            self.ranges = self.ranges + [tranges[0]] if len(tranges) == 2 else []
        self.ranges.append(tranges[-1] if len(tranges) else [])
    def end(self):
        return self.ranges[-1][-1]

    def start(self):
        return self.ranges[0][0]

    def intersect(self, a):
        tranges = self.ranges
        self.ranges = []
        for z in tranges:
            temp = z.intersect(a)
            if temp:
                self.ranges.append(temp)
        return bool(len(self.ranges))

    def length(self):
        length = 0
        for range in self.ranges:
            length += abs(range.end - range.start) + 1
        return length


def addRange(pair,array):
    if not pair:
        return
    for i in range(pair[1] - pair[0] + 1):
        if array[OFFSET + pair[0] + i] == '.':
            array[OFFSET + pair[0] + i] = '#'
def getRange(sensor, beacon, array):
    d = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    if abs(ROWINDEX - sensor[1]) > d:
        return None
    left = sensor[0] - (d - abs(ROWINDEX - sensor[1]))
    right = sensor[0] + (d - abs(ROWINDEX - sensor[1]))
    if sensor[1] == ROWINDEX:
        array[OFFSET + sensor[0]] = 'S'
    if beacon[1] == ROWINDEX:
        array[OFFSET + beacon[0]] = 'B'
    return (left,right)

def applySensor(sensor,beacon,ranges):
    d = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    for i in range(d + 1):
        left = sensor[0] - (d - i)
        right = sensor[0] + (d - i)
        ranges[OFFSETY + sensor[1] + i].add(Range(left, right))
        if i != 0:
            ranges[OFFSETY + sensor[1] - i].add(Range(left, right))

if __name__ == '__main__':
    print('Running AOC Day 15')
    filename = Path.joinpath(Path.cwd(), 'input/Day15.txt')
    ROWINDEX = 2000000  # 2000000 Puzzle  10 Test
    MAXINDEX = 4000000  # 4000000 Puzzle  20 Test
    with open(filename, 'r') as file:
        coords = [ [int(z) for z in re.compile('(-?\\d+)').findall(line)] for line in file.readlines() ]
    OFFSET = max([ max([x[0], x[2]]) for x in coords ]) - min([ min([x[0],x[2]]) for x in coords]) + 1
    OFFSETY = max([max([x[1], x[3]]) for x in coords ]) - min([min([x[1], x[3]]) for x in coords]) + 1
    # Array = ['.' for i in range( OFFSET  * 3 ) ]
    # NewArray = [RangeSet() for x in range(OFFSETY * 3)]
    # for sensor in coords:
    #     addRange( getRange((sensor[0],sensor[1]),(sensor[2],sensor[3]), Array), Array )
    # print("RowIndex: ", ROWINDEX)
    # print("Number of positions not containing a beacon: ", sum([1 for x in Array if x == '#']))

    # for sensor in coords:
    #     applySensor((sensor[0], sensor[1]), (sensor[2], sensor[3]), NewArray)
    #
    # WINDOW = Range(0, MAXINDEX)
    #
    # #tilesToTakeAway = sum([1 for x in coords if x[1] == ROWINDEX or x[3] == ROWINDEX])
    # tilesToTakeAway = set()
    # for row in coords:
    #     if row[1] == ROWINDEX:
    #         tilesToTakeAway.add(tuple([row[0], row[1]]))
    #     if row[3] == ROWINDEX:
    #         tilesToTakeAway.add(tuple([row[2], row[3]]))
    #
    # print("Number of positions not containing a beacon in row ", ROWINDEX, ": ", NewArray[OFFSETY + ROWINDEX].length() - len(tilesToTakeAway))
    # for i, range in enumerate(NewArray[OFFSETY:OFFSETY * 2]):
    #     range.intersect(WINDOW)
    #     if len (range.ranges) > 1:
    #         print("Beacon location found: (", range.ranges[0].end + 1, ", ", i, ").")
    #         print("Their Freq is: ", (range.ranges[0].end + 1 ) * 4000000 + i )
    #         #break

    # jtest = RangeSet()
    # jtest.add(Range(3, 7))
    # jtest.add(Range(12, 13))
    # jtest.add(Range(9, 10))
    # jtest.add(Range(2, 8))
    # print(jtest.ranges)
    # jtest.add(Range(-14, -8))
    # print(jtest.ranges)
    # jtest.add(Range(0, 20))
    # print(jtest.ranges)
    # jtest.intersect(Range(5, 10))
    # print(jtest.ranges)

    #create a list of sensor coords and their excluded "distance"
    sensors = [[x[0], x[1], abs(x[0] - x[2]) + abs(x[1] - x[3])] for x in coords]
    #
    curPos = 0
    # loop over row 0 to 4000000
    solved = False
    for row in range(0, MAXINDEX + 1):
        # in each row, loop over each sensor
        # if it reaches, add to candidates & order candidates by left-most index
        touchingSensors = [[x[0], x[1], x[0] - (x[2] - abs(x[1] - row)), x[2] - abs(x[1] - row) ] for x in sensors if abs(x[1] - row) <= x[2]]
        curPos = 0
        touchingSensors.sort(key=lambda x: x[2])
        # loop through candidates, if there is a gap, stop and report it
        for sens in touchingSensors:
            if curPos == sens[2] - 2:
                solved = True
                break
            curPos = sens[0] + sens[3] if sens[0] + sens[3] > curPos else curPos
        if solved:
            print('The x, y position is ', curPos + 1, row)
            print('The tuning frequency is: ', (curPos + 1) * 4000000 + row)
            solved = False

