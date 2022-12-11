
'''
read the file
evaluate score
1 A X Rock
2 B Y Paper
3 C Z Scissors
'''

class Game:
    SHAPES = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    NAMES = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
    OPTIONS = { 1: 'A', 2:'B', 3:'C'}

    def __init__(self, input):
        input = input.strip()
        if len(input) != 3:
            raise Exception('bad input')
        self.input = input
        self.you = input[2]
        self.foe = input[0]
        self.debug = self.NAMES[self.foe] + ' vs ' + self.NAMES[self.you]

    def score(self):
        #tie
        if Game.SHAPES[self.you] == Game.SHAPES[self.foe]:
            self.result = 'T'
            return 3 + Game.SHAPES[self.you]
        #win
        elif Game.SHAPES[self.you] % 3 == (Game.SHAPES[self.foe] + 1) % 3:
            self.result = 'W'
            return 6 + Game.SHAPES[self.you]
        #lose
        else:
            self.result = 'L'
            return 0 + Game.SHAPES[self.you]

    def score2(self):
        #win
        if self.you == 'Z':
            self.result = 'W'
            val = ( Game.SHAPES[self.foe] % 3 ) + 1
            self.choice = Game.OPTIONS[val]
            return 6 + val
        #tie
        if self.you == 'Y':
            self.result = 'T'
            val = Game.SHAPES[self.foe]
            self.choice = Game.OPTIONS[val]
            return 3 + val
        #lose
        if self.you == 'X':
            self.result = 'L'
            val = ( Game.SHAPES[self.foe] + 1) % 3 + 1
            self.choice = Game.OPTIONS[val]
            return val