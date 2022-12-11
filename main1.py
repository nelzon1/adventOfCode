def running(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Running: {name}')  # Press Ctrl+F8 to toggle the breakpoint.

from pathlib import Path
import aoc.Day1 as d1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    running('AOC Day 1')
    filename = Path.joinpath( Path.cwd(), 'input/Day1.txt')
    day1Reader = d1.Day1Reader(filename)
    day1Reader.readFile()
    #finalData = zip(range(len(day1Reader.elves)),[x.calories for x in day1Reader.elves])
    #part 1
    print('Max Calories: ', max([x.calories for x in day1Reader.elves]))

    #part 2
    sortedList = sorted(day1Reader.elves, key=lambda x: x.calories, reverse=True)
    topThree = sum([x.calories for x in sortedList[0:3]])
    print('Top 3 Calories: ', topThree)