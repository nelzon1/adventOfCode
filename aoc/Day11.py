from pathlib import Path
import functools as ft

class Monkey:

    def __init__(self, operation, test, ID, divisor, items=[]):
        self.items = [Item(x) for x in items]
        self.operation = operation
        self.test = test
        self.inspections = 0
        self.ID = ID
        self.divisor = divisor

    def addItem(self, item):
        self.items.append(item)

    def worryFactor(self):
        return sum([x.worry for x in self.items])

    def inspect(self):
        self.inspections += 1

class Item:

    def __init__(self, worry=0):
        self.worry = worry

    def updateWorry(self,value):
        self.worry = value

def test0(n):
    return 1 if n % 2 == 0 else 4
def test1(n):
    return 3 if n % 7 == 0 else 5
def test2(n):
    return 4 if n % 11 == 0 else 0
def test3(n):
    return 7 if n % 19 == 0 else 6
def test4(n):
    return 5 if n % 3 == 0 else 1
def test5(n):
    return 3 if n % 5 == 0 else 6
def test6(n):
    return 7 if n % 17 == 0 else 2
def test7(n):
    return 2 if n % 13 == 0 else 0

def fprint(monkeys):
    for monkey in monkeys:
        print('ID: ', monkey.ID, ' inspections: ', monkey.inspections, ' items: ', [x.worry for x in monkey.items])
    print(''.join(['-']*40))


if __name__ == '__main__':
    print('Running AOC Day 11')
    filename = Path.joinpath(Path.cwd(), 'input/Day11.txt')
    monkeys = []
    monkeys.append(Monkey(lambda x: x * 3, test0, 0, 2, [66, 59, 64, 51]))
    monkeys.append(Monkey(lambda x: x * 19, test1, 1, 7, [67, 61]))
    monkeys.append(Monkey(lambda x: x + 2, test2, 2, 11, [86, 93, 80, 70, 71, 81, 56]))
    monkeys.append(Monkey(lambda x: x * x, test3, 3, 19, [94]))
    monkeys.append(Monkey(lambda x: x + 8, test4, 4, 3, [71, 92, 64]))
    monkeys.append(Monkey(lambda x: x + 6, test5, 5, 5, [58, 81, 92, 75, 56]))
    monkeys.append(Monkey(lambda x: x + 7, test6, 6, 17, [82, 98, 77, 94, 86, 81]))
    monkeys.append(Monkey(lambda x: x + 4, test7, 7, 13, [54, 95, 70, 93, 88, 93, 63, 50]))
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
                item.updateWorry(monkey.operation(item.worry) % GLOBAL_LCM ) #// 3)
                target = monkey.test(item.worry)
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

