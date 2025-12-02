import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument(
    '--test', type=bool, dest='test_mode', default=False, action=argparse.BooleanOptionalAction,
)
parser.add_argument(
    '--debug', type=bool, dest='debug_mode', default=False, action=argparse.BooleanOptionalAction,
)
parser.add_argument('--start', type=int, dest='start_value', default=0)

args = parser.parse_args()

input_file = f"input/{'test' if args.test_mode else 'input'}.txt"

current_value = args.start_value
zero_count = 0
with open(input_file, 'r') as data:
    for line in data:
        if args.debug_mode:
            print(f"< {line};")
        direction, clicks = line[0], int(line[1:])
        if args.debug_mode:
            print(f"<< {direction}: {clicks};")
        match direction:
            case 'L': clicks = -clicks
            case 'R': pass
            case _: raise ValueError(f"invalid direction: {direction}")
        if args.debug_mode:
            print(f"<<< {current_value} + {clicks}")
        current_value += clicks
        if args.debug_mode:
            print(f"<<< {current_value=} before modulo")
        current_value %= 100
        if args.debug_mode:
            print(f"<<< {current_value=} after modulo")

        if current_value == 0:
            zero_count += 1
            if args.debug_mode:
                print(f"< {current_value=} stopped at 0; {zero_count=}")
                time.sleep(1)

print(f"zero count: {zero_count}")


