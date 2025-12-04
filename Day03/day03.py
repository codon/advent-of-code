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
    batteries = [_ for _ in range(0, m)]
    if args.debug_mode:
        print(f"{data=} {joltage(data, batteries)}")
    for ii in range(m, n):  # 12, 13, .., 100
        if args.debug_mode:
            print(f"{ii=} {batteries=}; {data[ii]} > {data[batteries[-1]]} ?")

        if data[ii] > data[batteries[-1]]:
            batteries[-1] = ii
            if args.debug_mode:
                print(f"new joltage: {joltage(data, batteries)}")

        # m=12, n=15
        # data=     '2  3  4  2  3  4  2  3  4  2   3   4   2  7  8'
        # batteries=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,     11, 12]
        # joltage == 234234234234
        # joltage == 234234234242
        for jj in range(m - 2, -1, -1):  # 10, 9, 8, .. 0
            # jj = 9
            # data[jj + 1] = 3
            # data[jj] = 2
            #
            if args.debug_mode:
                print(f"{ii=},{jj=}: {data[batteries[jj]+1]} > {data[batteries[jj]]} ?")
            if data[batteries[jj]+1] > data[batteries[jj]]:
                batteries[jj+1], batteries[jj] = batteries[jj+1]+1, batteries[jj+1]
                # need to cascade down so long as there is space
                if args.debug_mode:
                    print(f"new joltage: {joltage(data, batteries)}")

    return int(joltage(data, batteries))

checksum = 0
with open(input_file, 'r') as data:
    for line in map(lambda _: _.strip(), data):
        value = (check_part_1 if args.part == 1 else check_part_2)(line)
        checksum += value
        if args.debug_mode:
            print(f"{line=}; {value=} {checksum=}")

print(f"{checksum = }")
