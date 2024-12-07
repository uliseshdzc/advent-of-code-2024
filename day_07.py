from collections import deque
from common.utils import get_input

input = get_input(day=7)
data = [(int(a), list(map(int, b.split()))) for line in input.splitlines() for a, b in [line.split(":")]]

def get_calibration(include_concatenation: bool = False) -> int:
    result = 0
    for expected, values in data:
        stack = deque([expected])
        for value in values[:0:-1]:
            new_stack = set()
            while stack:
                current = stack.popleft()
                if value < current: new_stack.add(current - value)
                if current % value == 0: new_stack.add(current // value)
                if include_concatenation:
                    value_str, current_str = str(value), str(current)
                    if len(current_str) > len(value_str) and current_str[-len(value_str):] == value_str:
                        new_stack.add(int(current_str[:-len(value_str)]))
            stack = deque(new_stack)
        if values[0] in stack: result += expected
        
    return result

print(f"Part 1: {get_calibration()}")
print(f"Part 2: {get_calibration(True)}")