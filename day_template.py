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

def check_part_1(data: str) -> int:
    pass

def check_part_2(data: str) -> int:
    pass

checksum = 0
with open(input_file, 'r') as data:
    for line in map(lambda _: _.strip(), data):
        value = (check_part_1 if args.part == 1 else check_part_2)(line)
        checksum += value
        if args.debug_mode:
            print(f"{line=}; {value=} {checksum=}")

print(f"{checksum = }")
