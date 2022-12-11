from pathlib import Path
import re


class SchedulePair:
    digitRE = re.compile('(\\d+)')

    def __init__(self, inputStr):
        digits = [int(x) for x in re.findall(SchedulePair.digitRE, inputStr)]
        self.digits = digits
        self.overlaps = (digits[0] <= digits[2] and digits[1] >= digits[3]) \
                        or (digits[0] >= digits[2] and digits[1] <= digits[3])
        self.overlaps2 = digits[1] >= digits [2] and digits [0] <= digits [3]


if __name__ == '__main__':
    print('Running AOC Day 4')
    filename = Path.joinpath(Path.cwd(), 'input/Day4.txt')
    schedulePairs = []
    with open(filename, 'r') as file:
        for pair in file.readlines():
            schedulePairs.append(SchedulePair(pair))
    overlapCount = sum([1 for x in schedulePairs if x.overlaps])
    overlapCount2 = sum([1 for x in schedulePairs if x.overlaps2])
    print('Total number of completely overlapping pairs: ', overlapCount)
    print('Total number of overlapping pairs: ', overlapCount2)
