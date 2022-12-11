from pathlib import Path


class Buffer4:

    def __init__(self, str=''):
        self.chars = str.split()

    def addChar(self,char):
        self.chars.append(char)
        if len(self.chars) > 4:
            self.chars = self.chars[1:]

    def isValid(self):
        return len(self.chars) == 4 and len(self.chars) == len(set(self.chars))

class Buffer14:

    def __init__(self, str=''):
        self.chars = str.split()

    def addChar(self,char):
        self.chars.append(char)
        if len(self.chars) > 14:
            self.chars = self.chars[1:]

    def isValid(self):
        return len(self.chars) == 14 and len(self.chars) == len(set(self.chars))


if __name__ == '__main__':
    print('Running AOC Day 6')
    filename = Path.joinpath(Path.cwd(), 'input/Day6.txt')
    puzzle = ''
    with open(filename, 'r') as file:
        puzzle = file.readline()

    #Part 1
    buffer4 = Buffer4()
    count = 0
    for char in puzzle:
        count += 1
        buffer4.addChar(char)
        if buffer4.isValid():
            break

    print('Packet Key found: ', ''.join(buffer4.chars))
    print('Characters passed: ', count)

    #Part 2
    buffer14 = Buffer14()
    count = 0
    for char in puzzle:
        count += 1
        buffer14.addChar(char)
        if buffer14.isValid():
            break

    print('Message Key found: ', ''.join(buffer14.chars))
    print('Characters passed: ', count)
