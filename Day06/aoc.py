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

def cephalomath(data: list[int], oper) -> int:
    total = 1 if (oper == "*" or oper == "/") else 0

    if args.debug_mode:
        print(f'{data = }, {oper = }')

    for value in data:
        if oper == "*":
            total *= value
        elif oper == "/":
            total /= value
        elif oper == "+":
            total += value
        elif oper == "-":
            total -= value
    if args.debug_mode:
        print(f'{total = }')

    return total

def check_part_1(data: list[list[int]], opers: list[str]) -> int:
    if args.debug_mode:
        print(f'{data = }')
        print(f'{opers = }')

    n = len(opers)
    totals = [0] * n

    for ii in range(n):
        totals[ii] = cephalomath([d[ii] for d in data], opers[ii])

    if args.debug_mode:
        print(f'{totals = }')

    sum_totals = sum(totals)
    if args.debug_mode:
        print(f'{sum_totals = }')
    return sum_totals

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
    for line in map(lambda _: _.rstrip(), data):
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
