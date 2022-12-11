'''
Read in file, make an elf for each group of numbers and reset on a blank
'''

class Day1Reader:

    def __init__(self, filename):
        self.elves = []
        self.file = open(filename,'r')

    def destroy(self):
        self.file.close()

    def readFile(self):
        #first elf
        self.elves.append( Elf() )
        index = 0
        for line in self.file.readlines():
            if len(line) <= 2:
                #next elf
                self.elves.append( Elf() )
                index += 1
            else:
                self.elves[index].addCalories(int(line))


class Elf:

    def __init__(self):
        self.calories = 0

    def addCalories(self, cal):
        self.calories += cal