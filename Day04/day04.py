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

deltas = [(dx, dy) for dx in range (-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0)]

def score_grid(data: list[list[str]], scores: list[list[int]]) -> int:
    rows, cols = len(data), len(data[0])
    score = 0

    for y in range(rows):
        for x in range(cols):
            if data[y][x] != '@':
                continue
            scores[y][x] = sum(
                [1 for dx, dy in deltas if 0 <= y + dy < rows and 0 <= x + dx < cols and data[y + dy][x + dx] == '@']
            )
            if scores[y][x] < 4:
                score += 1

        if args.debug_mode:
            print(f"{data[y]} {scores[y]} {score}")

    return score

def remove_rolls(data: list[list[str]], scores: list[list[int]]) -> None:
    rows, cols = len(data), len(data[0])
    for y in range(rows):
        for x in range(cols):
            if data[y][x] != '@':
                continue
            if scores[y][x] < 4:
                if args.debug_mode:
                    print(f'remove roll[{y}][{x}]: {data[y][x]} => "-"')
                data[y][x] = '-'
                scores[y][x] = 0

def check_part_1(data: list[list[str]], scores: list[list[int]]) -> int:
    return score_grid(data, scores)

def check_part_2(data: list[list[str]], scores: list[list[int]]) -> int:
    total_rolls = 0
    while score := score_grid(data, scores):
        remove_rolls(data, scores)
        total_rolls += score
    return total_rolls

checksum = 0
grid: list[list[str]] = []
scores: list[list[int]] = []

with open(input_file, 'r') as data:
    for line in map(lambda _: _.strip(), data):
        grid.append([*line])
        scores.append([0]*len(line))

    value = (check_part_1 if args.part == 1 else check_part_2)(grid, scores)
    checksum += value
    if args.debug_mode:
        print(f"{grid}\n{value=} {checksum=}")

print(f"{checksum = }")
