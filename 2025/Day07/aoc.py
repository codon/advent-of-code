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

def check_part_1(tick: str, existing: list[str]) -> tuple[int, list[str]]:
    new = existing.copy()
    n = len(tick)
    splits = 0
    for ii in range(n):
        if tick[ii] == 'S':
            new[ii] = 1
        elif tick[ii] == '^' and existing[ii] == 1:
            splits += 1
            if ii - 1 >= 0:
                new[ii-1] = 1
            new[ii] = 0
            if ii + 1 < n:
                new[ii+1] = 1
    return (splits, new)


def check_part_2(tick: str, existing: list[str]) -> tuple[int, list[str]]:
    new = existing.copy()
    n = len(tick)
    splits = 0
    for ii in range(n):
        if tick[ii] == 'S':
            new[ii] = 1
        elif tick[ii] == '^' and existing[ii] != 0:
            splits += new[ii] * 2
            if ii - 1 >= 0:
                new[ii-1] += new[ii]
            if ii + 1 < n:
                new[ii+1] += new[ii]
            new[ii] = 0
    return (splits, new)

checksum = 0
with open(input_file, 'r') as data:
    beams = []
    for line in map(lambda _: _.strip(), data):
        if len(beams) == 0:
            beams = [0] * len(line)
        if args.debug_mode:
            print(line)

        if args.part == 1:
            splits, beams = check_part_1(line, beams)
            checksum += splits
        else:
            splits, beams = check_part_2(line, beams)
            checksum = sum(beams)

        if args.debug_mode:
            print(f"{''.join(map(str,beams))} {splits=} {checksum=}")

print(f"{checksum = }")
