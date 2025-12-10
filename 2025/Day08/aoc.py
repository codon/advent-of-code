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

def distance(a:tuple[int,int,int], b:tuple[int,int,int]) -> float:
    return ( (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2 ) ** 0.5

def check_part_1(data: str) -> int:
    pass

def check_part_2(data: str) -> int:
    pass

checksum = 0
deltas = {}
junctions = []
with open(input_file, 'r') as data:
    for line in map(lambda _: _.strip(), data):
        x,y,z = map(int,line.split(','))
        for other in junctions:
            x1,y1,z1 = map(int,other.split(','))
            delta = distance([x,y,z], [x1,y1,z1])
            deltas[delta] = [line, other]
            if args.debug_mode:
                print(f'{line} -> {other} = {delta}')
        junctions.append(line)

if args.debug_mode:
    for key in sorted(deltas.keys()):
        print(f'{key} => {deltas[key]}')

"""
value = (check_part_1 if args.part == 1 else check_part_2)(line)
checksum += value
if args.debug_mode:
    print(f"{line=}; {value=} {checksum=}")
"""

print(f"{checksum = }")
