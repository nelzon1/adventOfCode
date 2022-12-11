from pathlib import Path

if __name__ == '__main__':
    print('Running AOC Day 0')
    filename = Path.joinpath(Path.cwd(), 'input/Day0.txt')
    puzzle = ''
    with open(filename, 'r') as file:
        puzzle = file.readline()
