from pathlib import Path
import functools as ft

class Monkey:

    def __init__(self, operation, test, ID, divisor, cmd, items=[]):
        self.items = [Item(x) for x in items]
        self.operation = operation
        self.test = test
        self.inspections = 0
        self.ID = ID
        self.divisor = divisor
        self.cmd = cmd

    def addItem(self, item):
        self.items.append(item)

    def worryFactor(self):
        return sum([x.worry for x in self.items])

    def inspect(self):
        self.inspections += 1

class Item:

    def __init__(self, worry=0):
        self.worry = worry
        self.operations = []
        self.inspections = 0

    def updateWorry(self,value):
        self.worry = value

    def isDivisible(self, n):
        val = self.worry
        for expr in self.operations:
            if expr[0] == '*':
                if expr[1] == 's':
                    val = ((val % n) * 2) #% n
                else:
                    num = int(expr[1:])
                    val = ((val % n) * (num % n)) #% n
            elif expr[0] == '+':
                num = int(expr[1:])
                #add
                val = ((val % n) + (num % n)) #% n
        return not bool(val % n)

    def inspect(self,cmd):
        self.operations.append(cmd)
        self.inspections += 1
def test0(n):
    return 2 if n % 23 == 0 else 3
def test1(n):
    return 2 if n % 19 == 0 else 0
def test2(n):
    return 1 if n % 13 == 0 else 3
def test3(n):
    return 0 if n % 17 == 0 else 1

def fprint(monkeys):
    for monkey in monkeys:
        print('ID: ', monkey.ID, ' inspections: ', monkey.inspections, ' items: ', [x.worry for x in monkey.items])
    print(''.join(['-']*40))


if __name__ == '__main__':
    print('Running AOC Day 11')
    filename = Path.joinpath(Path.cwd(), 'input/Day11.txt')
    monkeys = []
    monkeys.append(Monkey(lambda x: x * 19, test0, 0, 23, '*19', [79, 98]))
    monkeys.append(Monkey(lambda x: x + 6, test1, 1, 19, '+6', [54, 65, 75, 74]))
    monkeys.append(Monkey(lambda x: x * x, test2, 2, 13, '*s', [79, 60, 97]))
    monkeys.append(Monkey(lambda x: x + 3, test3, 3, 17, '+3', [74]))
    '''
    for x rounds
        for each monkey
            for each item
                update its worry
                determine who it goes to
                assign it over
    '''
    ROUNDS = 10000
    GLOBAL_LCM = ft.reduce(lambda x, y: x * y, [x.divisor for x in monkeys])
    for round in range(ROUNDS):
        for monkey in monkeys:
            for i in range(len(monkey.items)):
                item = monkey.items[0]
                monkey.inspect()
                item.inspect(monkey.cmd)
                item.updateWorry(monkey.operation(item.worry) % GLOBAL_LCM ) #Part 2 // 3)
                target = monkey.test(item.worry)
                #target = monkey.test(item.isDivisible(monkey.divisor))
                monkeys[target].addItem(monkey.items.pop(0))
                #fprint(monkeys)
        if (round+1) == 20 or (round+1) % 1000 == 0:
            print(round+1,' rounds complete.')
            fprint(monkeys)


    cnt = 0
    for monkey in monkeys:
        print('Monkey',cnt,' inspections: ', monkey.inspections)
        cnt += 1
    #monkeys.sort(key=lambda x: x.inspections, reverse=True)
    monkeyBusiness = sorted(monkeys, key=lambda x: x.inspections, reverse=True)[0:2]
    print('Monkey Business after ',ROUNDS,' rounds: ', monkeyBusiness[0].inspections * monkeyBusiness[1].inspections)
    print()
    fprint(monkeys)

