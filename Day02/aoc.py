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

invalid_id_sum = 0

def check_part_1(candidate_id: str) -> None:
    global invalid_id_sum
    if len(candidate_id) % 2:
        return
    mid = len(candidate_id) // 2
    if candidate_id[0:mid] == candidate_id[mid:]:
        invalid_id_sum += int(candidate_id)
        if args.debug_mode:
            print(f"invalid_id: {candidate_id}; checksum: {invalid_id_sum}")

def check_part_2(candidate_id: str) -> None:
    global invalid_id_sum
    length = len(candidate_id)
    mid = length // 2

    if length < 2:
        return

    if mid < 2:
        if candidate_id[0] == candidate_id[1] == candidate_id[length-1]:
            invalid_id_sum += int(candidate_id)
            if args.debug_mode:
                print(f"invalid_id: {candidate_id}; checksum: {invalid_id_sum}")
            return

    if length % 2:
        if candidate_id == candidate_id[0] * length:
            invalid_id_sum += int(candidate_id)
            if args.debug_mode:
                print(f"invalid_id: {candidate_id}; checksum: {invalid_id_sum}")

    for n in range(2, mid+1):
        if args.debug_mode:
            # print(f"{candidate_id=}: {n=} {length=} {length % n=}")
            pass
        if length % n:
            # don't check if length not evenly divisible by n
            continue

        pattern = candidate_id[0:n]
        repetitions = length // n
        if args.debug_mode:
            # print(f"check {candidate_id=}; {pattern=} {repetitions=}")
            pass

        if candidate_id == pattern * repetitions:
            invalid_id_sum += int(candidate_id)
            if args.debug_mode:
                print(f"invalid_id: {candidate_id}; checksum: {invalid_id_sum}")
            break


with open(input_file, 'r') as data:
    for line in data:
        line.replace("\n",'')
        for id_range in line.split(','):
            if args.debug_mode:
                print(f'{id_range=}')
                pass
            start_id, stop_id = list(map(lambda _: int(_), id_range.split('-')))
            if args.debug_mode:
                print(f'{start_id=} .. {stop_id=}')
                pass
            for candidate_id in map(lambda _: str(_), range(start_id, stop_id + 1)):
                if args.debug_mode:
                    # print(f"check {candidate_id=}")
                    pass
                check_part_1(candidate_id) if args.part == 1 else check_part_2(candidate_id)
                # time.sleep(1)

print(f"checksum: {invalid_id_sum}")
