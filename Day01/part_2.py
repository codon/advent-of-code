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
        direction, clicks = line[0], int(line[1:])
        if args.debug_mode:
            print(f"> {current_value=}; {direction}: {clicks};")
        if clicks >= 100:
            additional_zeros = clicks // 100
            zero_count += clicks // 100
            print(f">> passing {current_value} {additional_zeros} times; {zero_count=}")
            clicks %= 100
            print(f">> effective change: {current_value=}; {direction}: {clicks};")
        match direction:
            case 'L': clicks = -clicks
            case 'R': pass
            case _: raise ValueError(f"invalid direction: {direction}")

        # Edge case: starting from zero; L turn -> negative; counting extra "passed zero"
        started_at_zero = current_value == 0
        current_value += clicks

        if current_value < 0 and not started_at_zero:
            zero_count += 1
            if args.debug_mode:
                print(f"<<< {current_value=} passed by zero going negative; {zero_count=}")
        elif current_value >= 100:
            zero_count += 1
            if args.debug_mode:
                print(f"<<< {current_value=} passed by zero going positive; {zero_count=}")
        elif current_value == 0:
            zero_count += 1
            if args.debug_mode:
                print(f"< {current_value=} stopped at 0; {zero_count=}")

        current_value %= 100

print(f"zero count: {zero_count}")


