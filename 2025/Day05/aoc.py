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

ii = 0
checksum = 0
fresh: list[tuple[int,int]] = []
parse_fresh = True

def check_part_1(ingredient: int) -> int:
    global ii
    if ingredient < fresh[ii][0]:
        if args.debug_mode:
            print(f"ingredient {ingredient} < fresh[{ii}][0]: {fresh[ii][0]}; spoiled")
        return 0

    while ii < len(fresh) and ingredient > fresh[ii][1]:
        if args.debug_mode:
            print(f"ingredient {ingredient} > fresh[{ii}][0]: {fresh[ii][0]}")
        ii += 1

    if ii < len(fresh) and fresh[ii][0] <= ingredient <= fresh[ii][1]:
        if args.debug_mode:
            print(f"ingredient {ingredient} is available and fresh")
        return 1

    if args.debug_mode:
        print(f"ingredient {ingredient} is spoiled")

    return 0


def check_part_2() -> int:
    fresh_count = 0
    for start, stop in fresh:
        count = stop + 1 - start
        fresh_count += count
        if args.debug_mode:
            print(f"({start} .. {stop}) = {count}; {fresh_count=}")

    return fresh_count

with open(input_file, 'r') as data:
    for line in map(lambda _: _.strip(), data):
        if line == "":
            if args.debug_mode:
                print(f"{fresh = }")
            parse_fresh = False
            continue

        if parse_fresh:
            first, last = map(lambda _: int(_), line.split('-'))
            if len(fresh) > 0 and first <= fresh[-1][1]:
                if last > fresh[-1][1]:
                    fresh[-1] = (fresh[-1][0], last)
            else:
                fresh.append((first, last))

        else:
            if args.part == 1:
                value = check_part_1(int(line))
                checksum += value
                if args.debug_mode:
                    print(f"{value=} {checksum=}")
            else:
                break

if args.part == 2:
    checksum = check_part_2()

print(f"{checksum = }")
