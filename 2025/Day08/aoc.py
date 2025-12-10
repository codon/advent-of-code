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

def distance(a:tuple[int,int,int], b:tuple[int,int,int]) -> int:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

def check_part_1(data: dict[int, set[str]], limit: int) -> int:
    connections = 0
    circuits: list[set[str]] = []
    for _, junctions in [(k, data[k]) for k in sorted(data.keys())]:
        bridges = list(filter(lambda _: junctions & circuits[_], range(len(circuits))))
        if bridges:
            if args.debug_mode:
                print(f'new circuit {junctions} connects to {[circuits[_] for _ in bridges]}')
            new_circuit = junctions
            for n in bridges:
                new_circuit.update(circuits[n])
            circuits[bridges[0]] = new_circuit
            if len(bridges) > 1:
                circuits[bridges[1]:1] = []
        else:
            circuits.append({*junctions})
            if args.debug_mode:
                print(f'create new circuit {circuits[-1]} from {junctions}')

        connections += 1
        if connections >= limit:
            break

    if args.debug_mode:
        for _ in circuits:
            print(_)

    checksum = 1
    for _ in map(len, sorted(circuits, reverse=True, key=len)[:3]):
        checksum *= _
        if args.debug_mode:
            print(f'circuit size: {_}; {checksum = }')

    return checksum

def check_part_2(data: str) -> int:
    pass

deltas: dict[int, set[str]] = {}
max_connections = 10 if args.test_mode else 1000

junctions = []
with open(input_file, 'r') as data:
    for line in map(lambda _: _.strip(), data):
        x,y,z = map(int,line.split(','))
        for other in junctions:
            x1,y1,z1 = map(int,other.split(','))
            delta = distance([x,y,z], [x1,y1,z1])
            if deltas.get(delta) is None:
                deltas[delta] = {line, other}
            else:
                deltas[delta].update([line, other])
            if args.debug_mode:
                # print(f'{line} -> {other} = {delta}')
                pass
        junctions.append(line)

if args.debug_mode:
    n = 0
    for key in sorted(deltas.keys()):
        print(f'{key} => {deltas[key]}')
        n += 1
        if (args.test_mode == 1 and n >= 10) or n >= 1000:
            break

checksum = 0
if args.part == 1:
    checksum = check_part_1(deltas, max_connections)
else:
    checksum = check_part_2(deltas, len(junctions))

print(f"{checksum = }")
