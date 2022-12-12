from pathlib import Path

class Computer:
    #register X
    def __init__(self):
        self.registerX = 1
        self.clock = 1
        self.signalSum = 0
        self.screen = [[0 for x in range(40)] for x in range(6)]

    def clockTick(self):
        if (self.clock - 20) % 40 == 0:
            print('Clock: ', self.clock, ' Register: ', self.registerX, ' signal: ', self.clock * self.registerX)
            self.signalSum += self.clock * self.registerX
        self.drawPixel()
        self.clock += 1

    def drawPixel(self):
        cursor = (self.clock - 1 ) % 40
        row =  (self.clock - 1) // 40
        if cursor >= self.registerX - 1 and cursor <= self.registerX + 1:
            self.screen[row][cursor] = '#'
        else:
            self.screen[row][cursor] = '.'

    def drawScreen(self):
        for row in self.screen:
            print('|->', row, '<-|')


    def noop(self):
        self.clockTick()

    def addV(self, val):
        self.clockTick()
        self.clockTick()
        self.registerX += val

    def parseCmd(self,strIn):
        if strIn[0] == 'a':
            self.addV(int(strIn.strip()[5:]))
        else:
            self.noop()

if __name__ == '__main__':
    print('Running AOC Day 10')
    filename = Path.joinpath(Path.cwd(), 'input/Day10.txt')
    cmdList = ''
    with open(filename, 'r') as file:
        cmdList = file.readlines()
    computer = Computer()
    for cmd in cmdList:
        computer.parseCmd(cmd)

    print('Sum of Signals: ', computer.signalSum)

    computer.drawScreen()
