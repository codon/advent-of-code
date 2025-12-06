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

def joltage(data: str, batteries: list[int]) -> str:
    return str.join('', list(map(lambda _: data[_], batteries)))

def check_part_1(data: str) -> int:
    n = len(data)
    a, b = data[0:2]
    for ii in range(2, n):
        if b > a:
            a, b = b, data[ii]
        if b < data[ii]:
            b = data[ii]
    return int(a+b)

def check_part_2(data: str) -> int:
    n = len(data)
    m = 12
    batteries = []

    if args.debug_mode:
        print(f"{data=} {joltage(data, batteries)}")
    for ii in range(m):
        if args.debug_mode:
            print(f"[{ii}] for jj in range({0 if len(batteries) == 0 else (batteries[-1] + 1)}, {n - m + len(batteries)}):")
        for jj in range(0 if len(batteries) == 0 else (batteries[-1] + 1), n - (m - ii)):
            if ii == len(batteries):
                batteries.append(jj)
                if args.debug_mode:
                    print(f"select next battery ({ii}). starting with data[{jj}]: {data[jj]}")
                    print(f"{batteries = }")
            if data[jj+1] > data[batteries[ii]]:
                if args.debug_mode:
                    print(f"battery {jj+1} has greater jolts ({data[jj+1]}) than batteries[{ii}] ({data[batteries[ii]]})")
                batteries[ii] = jj+1
        if len(batteries) <= ii:
            batteries.append(batteries[-1] + 1)

        if args.debug_mode:
            print(f"[{ii}] {batteries = }")
            print(f"[{ii}] new joltage: {joltage(data, batteries)}")

    return int(joltage(data, batteries))

checksum = 0
with open(input_file, 'r') as data:
    for line in map(lambda _: _.strip(), data):
        value = (check_part_1 if args.part == 1 else check_part_2)(line)
        checksum += value
        if args.debug_mode:
            print(f"{line=}; {value=} {checksum=}")

print(f"{checksum = }")
