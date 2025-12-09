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

def check_part_1(data: list[list[int]], opers: list[str]) -> int:
    n = len(opers)
    check, totals = 0, [1 if _ == "*" or _ == "/" else 0 for _ in opers]
    if args.debug_mode:
        print(f'{opers = }')
    for row in data:
        if args.debug_mode:
            print(f'{row = }')
        for ii in range(n):
            if opers[ii] == "*":
                totals[ii] *= row[ii]
            elif opers[ii] == "/":
                totals[ii] /= row[ii]
            elif opers[ii] == "+":
                totals[ii] += row[ii]
            elif opers[ii] == "-":
               totals[ii] -= row[ii]
        if args.debug_mode:
            print(f'{totals = }')

    sum_sum = sum(totals)
    if args.debug_mode:
        print(f'{sum_sum = }')
    return sum_sum

def check_part_2(data: list[list[int]], opers: list[str]) -> int:
    pass

rows: list[list[int]] = []
operators: list[str] = []
checksum = 0
with open(input_file, 'r') as data:
    for line in map(lambda _: _.strip(), data):
        if line[0] in "*/+-":
            operators = [_ for _ in line.split(" ") if _ != ""]
            if args.debug_mode:
                print(f'{operators = }')
        else:
            row = [int(_) for _ in line.split(" ") if _ != ""]
            rows.append(row)
            if args.debug_mode:
                print(f'{row = }')

checksum = (check_part_1 if args.part == 1 else check_part_2)(rows, operators)

print(f"{checksum = }")
