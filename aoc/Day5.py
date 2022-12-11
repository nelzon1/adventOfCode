from pathlib import Path
import re

instructionRE = re.compile('\\d+')

class Stack:
    def __init__(self):
        self.boxes = []


def parseLine(line):
    return [line[1+4*i] for i in range(9)]

def readInstructions(line):
    return tuple(int(x) for x in re.findall(instructionRE, line))


if __name__ == '__main__':
    print('Running AOC Day 5')
    filename1 = Path.joinpath(Path.cwd(), 'input/Day5B.txt')
    filename2 = Path.joinpath(Path.cwd(), 'input/Day5A.txt')
    stacks = [Stack() for i in range(9)]
    rows = []
    with open(filename1, 'r') as file:
        for row in file.readlines():
            rows.append(parseLine(row))
    index = 0
    for row in rows[::-1]:
        for char in row:
            if char == ' ':
                index += 1
                continue
            stacks[index].boxes.append(char)
            index += 1
        index = 0

    instructions = []
    with open(filename2, 'r') as file:
        for row in file.readlines():
            instructions.append(readInstructions(row))

    # Part 1
    # for inst in instructions:
    #     for move in range(inst[0]):
    #         stacks[inst[2]-1].boxes.append( stacks[inst[1]-1].boxes.pop() )

    # Part 2
    for inst in instructions:
        stacks[inst[2]-1].boxes += stacks[inst[1]-1].boxes[len(stacks[inst[1]-1].boxes)-inst[0]:]
        stacks[inst[1] - 1].boxes = stacks[inst[1]-1].boxes[:len(stacks[inst[1]-1].boxes)-inst[0]]
    print('The top of each stack: ')
    tops = [x.boxes[-1] for x in stacks]
    print (tops)