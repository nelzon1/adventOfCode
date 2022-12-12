from pathlib import Path

class Knot:
    def __init__(self, parent=None,x=0,y=0, child=None):
        self.parent = parent
        self.x = x
        self.y = y
        self.child = child
class Rope:
    def __init__(self):
        self.head = Knot()
        self.tail = self.head
        self.knots = [self.head]

    def addKnot(self, knot=Knot()):
        knot.parent = self.tail
        self.tail.child = knot
        self.tail = knot
        self.knots.append(knot)

    def moveTail(head, tail, moves):
        xDiff = head.x - tail.x
        yDiff = head.y - tail.y

        if abs(xDiff) + abs(yDiff) == 3:
            # move diagonal:
            if abs(xDiff) == 1:
                tail.x += xDiff
            else:
                tail.y += yDiff
        if abs(xDiff) == 2:
            tail.x += xDiff // 2
        if abs(yDiff) == 2:
            tail.y += yDiff // 2
        moves.add(tuple([tail.x, tail.y]))

    def moveHead(direction, head):
        if direction == 'L':
            head.x -= 1
        elif direction == 'R':
            head.x += 1
        elif direction == 'U':
            head.y += 1
        elif direction == 'D':
            head.y -= 1

def moveTail(head,tail,moves):
    xDiff = head[0] - tail[0]
    yDiff = head[1] - tail[1]

    if abs(xDiff) + abs(yDiff) == 3:
        #move diagonal:
        if abs(xDiff) == 1:
            tail[0] += xDiff
        else:
            tail[1] += yDiff
    if abs(xDiff) == 2:
        tail[0] += xDiff // 2
    if abs(yDiff) == 2:
        tail[1] += yDiff // 2
    moves.add(tuple(tail))

def moveHead(direction, head):
    if direction == 'L':
        head[0] -= 1
    elif direction == 'R':
        head[0] += 1
    elif direction == 'U':
        head[1] += 1
    elif direction == 'D':
        head[1] -= 1

if __name__ == '__main__':
    print('Running AOC Day 9')
    filename = Path.joinpath(Path.cwd(), 'input/Day9.txt')
    moveList = ''
    with open(filename, 'r') as file:
        moveList = file.readlines()

    #Part 1
    visited = set()
    head = [0,0]
    tail = [0,0]

    for move in moveList:
        direction = move[0]
        steps = int(move.strip()[2:])
        for i in range(steps):
            moveHead(direction, head)
            moveTail(head, tail, visited)

    print('Total number of tiles visited by tail: ', len(visited))

    #Part 2
    visited = set()
    tailVisited = set()
    head = [0,0]
    tail = [0,0]
    rope = Rope()
    ropeSize = 9
    [rope.addKnot(Knot()) for x in range(ropeSize)]

    for move in moveList:
        direction = move[0]
        steps = int(move.strip()[2:])
        for i in range(steps):
            Rope.moveHead(direction, rope.head)
            for knot in rope.knots[1:]:
                if knot.child == None:
                    Rope.moveTail(knot.parent, knot, tailVisited)
                Rope.moveTail(knot.parent, knot, visited)

    print('Total number of tiles visited by long tail: ', len(tailVisited))
