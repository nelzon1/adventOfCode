def running(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Running: {name}')  # Press Ctrl+F8 to toggle the breakpoint.

from pathlib import Path

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    running('AOC Day 4')
    filename = Path.joinpath( Path.cwd(), 'input/Day4.txt')

    backpacks = []
    with open(filename, 'r') as file:
        for backpack in file.readlines():
            backpacks.append(Backpack(backpack))

    priority = [x.priority() for x in backpacks]
    print('Total Priority: ', sum(priority))

    intersections = []
    for i in range(len(backpacks)):
        if i % 3 == 0:
            setA = set((backpacks[i].front + backpacks[i].back))
            setB = set((backpacks[i+1].front + backpacks[i+1].back))
            setC = set((backpacks[i+2].front + backpacks[i+2].back))
            temp = setA.intersection(setB)
            temp = temp.intersection(setC)
            temp.remove('\n')
            temp = list(temp)[0]
            intersections.append((temp,Backpack.elfPriority(temp)))

    print('Sum of badge priorities: ', sum([x[1] for x in intersections]))

