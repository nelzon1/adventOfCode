def running(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Running: {name}')  # Press Ctrl+F8 to toggle the breakpoint.

from pathlib import Path
import aoc.Day2 as d2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    running('AOC Day 2')
    filename = Path.joinpath( Path.cwd(), 'venv', 'input/Day2.txt')

    games = []
    with open(filename, 'r') as file:
        for game in file.readlines():
            games.append( d2.Game(game) )

    scores = [x.score() for x in games]
    scores2 = [x.score2() for x in games]
    debug = zip([x.input + ' '+ x.debug + ' ' + x.result for x in games], scores)
    debug2 = zip([x.input + ' ' + x.debug + ' ' + x.choice for x in games], scores2)
    print('My total score with Strat 1: ', sum(scores))

    print('My total score with Strat 2: ', sum(scores2))
    #
    # for game in debug2:
    #     print(game)

