# This code was based on the solution given by https://github.com/topaz
# at https://www.reddit.com/r/adventofcode/comments/1hj2odw/comment/m33uf55/
from collections import Counter
from common.utils import get_input

codes = get_input(day=21).splitlines()
numeric_keypad = {char: (i % 3, i // 3) for i, char in enumerate("789456123 0A")}
direction_keypad = {char: (i % 3, i // 3) for i, char in enumerate(" ^A<v>")}

def steps(keypad: dict[complex, str], commands: str, count=1) -> Counter[tuple[int, int, bool]]:
    current_x, current_y = keypad["A"]
    blank_x, blank_y = keypad[" "]
    counter = Counter()
    for command in commands:
        target_x, target_y = keypad[command]
        passes_blank = target_x == blank_x and current_y == blank_y \
            or target_y == blank_y and current_x == blank_x
        counter[(target_x - current_x, target_y - current_y, passes_blank)] += count
        current_x, current_y = target_x, target_y
    return counter


def calculate_button_presses(n_direction_keypads) -> int:
    result = 0
    for code in codes:
        step_counter = steps(numeric_keypad, code)
        for _ in range(n_direction_keypads + 1):
            step_counter = sum(
                (steps(
                    direction_keypad, 
                    ("<" * -x + "v" * y + "^" * -y + ">" * x)[::-1 if passes_blank else 1] + "A", 
                    step_counter[(x, y, passes_blank)]
                ) for x, y, passes_blank in step_counter), 
                Counter()
            )
        result += step_counter.total() * int(code[:3])
    return result

print(f"Part 1: {calculate_button_presses(n_direction_keypads=2)}")
print(f"Part 2: {calculate_button_presses(n_direction_keypads=25)}")