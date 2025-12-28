import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('--part', type=int, dest='part', default=1)

parser.add_argument(
    '--test', type=bool, dest='test_mode', default=False, action=argparse.BooleanOptionalAction,
)
parser.add_argument(
    '--debug', type=bool, dest='debug_mode', default=False, action=argparse.BooleanOptionalAction,
)

args = parser.parse_args()

input_file = f"input/{'test' if args.test_mode else 'input'}.txt"

def plot_tiles(grid: list[list[str]], tiles: list[tuple[int,int]]) -> None:
    for x,y in tiles:
        if y < len(grid) and x < len(grid[y]):
            grid[y][x] = '#'

def visualize_tiles(grid: list[list[str]]) -> None:
    for row in grid:
        print(''.join(row))

def area(args: tuple[tuple[int,int], tuple[int,int]]) -> int:
    a, b = args
    __ = (b[0] - a[0]) * (b[1] - a[1])
    print(f'area({args}) = {__}')
    return __


def check_part_1(data: str, minmax_x: tuple[int,int], minmax_y: tuple[int,int]) -> int:
    coordinates: dict[str, tuple[int,int]] = {}
    first, last = -1, -1
    for y in minmax_y:
        line = ''.join(data[y])
        first, last = line.find('#'), line.rfind('#')
        coordinates[f'{first},{y}'] = (first,y)
        coordinates[f'{last},{y}'] = (last,y)

    for x in minmax_x:
        line = ''.join(map(lambda _: _[x], data[0:minmax_y[1]+1]))
        first, last = line.find('#'), line.rfind('#')
        coordinates[f'{x},{first}'] = (x,first)
        coordinates[f'{x},{last}']  = (x,last)

    for key in sorted(coordinates.keys(), key=lambda _: coordinates[_][0]):
        print(f'{key} => {coordinates[key]}')
    foo = sorted(coordinates.keys(), key=lambda _: coordinates[_][0])
    a,b,c,d = map(lambda _: coordinates[foo[_]], [0,1,-1,-2])

    return max([area(_) for _ in [(a,c), (b,d)]])

def check_part_2(data: str, minmax_x: tuple[int,int], minmax_y: tuple[int,int]) -> int:
    return 0

checksum = 0
tiles: list[list[str]] = []
red_tiles: list[tuple[int,int]] = []
with open(input_file, 'r') as data:
    max_x, max_y = 0, 0
    min_x, min_y = -1, -1
    for line in map(lambda _: _.strip(), data):
        x,y = map(int, line.split(','))
        if min_x == -1:
            min_x = x
        if min_y == -1:
            min_y = y

        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y

        red_tiles.append((x,y))

tiles = [['.'] * (min_x+max_x+1) for _ in range(min_y+max_y+1)]
plot_tiles(tiles, red_tiles)

if args.debug_mode:
    visualize_tiles(tiles)
    print(f'{min_x=},{max_x=}; {min_y=},{max_y=}')

value = (check_part_1 if args.part == 1 else check_part_2)(tiles,(min_x,max_x),(min_y,max_y))
checksum += value
if args.debug_mode:
    print(f"{value=} {checksum=}")

print(f"{checksum = }")
