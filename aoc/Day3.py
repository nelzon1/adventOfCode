'''
backpack has 2 compartments
only 1 item will be duplicated at most

'''
class Backpack:

    def __init__(self, inputStr):
        inputLen = len(inputStr)
        self.front = inputStr[:inputLen//2]
        self.back = inputStr[inputLen//2:]
        self.check()

    def check(self):
        for char in self.front:
            if char in self.back:
                self.item = char
                return char
        return ''

    def elfPriority(n):
        if ord(n) > 96:
            return ord(n) - 96
        else:
            return ord(n) - 38

    def priority(self):
        if not self.item:
            return 0
        if ord(self.item) > 96:
            self.pri = ord(self.item) - 96
            return ord(self.item) - 96
        else:
            self.pri = ord(self.item) - 38
            return ord(self.item) - 38