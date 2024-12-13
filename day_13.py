import re
from itertools import starmap
from sympy import solve, Symbol
from common.utils import get_input

input = get_input(day=13)
configurations = [list(map(int, re.findall(r"\d+", configuration))) for configuration in input.split("\n\n")]

def token_value(ax: int, ay: int, bx: int, by: int, x: int, y: int, prize_shift: int = 0) -> int:
    x += prize_shift
    y += prize_shift
    a, b = Symbol('a', integer=True), Symbol('b', integer=True)

    roots = solve(
        [ax * a + b * bx - x, ay * a + by * b - y],
        [a, b]
    )

    return 3 * roots[a] + roots[b] if roots else 0

print(f"Part 1: {sum(token_value(*configuration) for configuration in configurations)}")
print(f"Part 2: {sum(token_value(*configuration, prize_shift=10000000000000) for configuration in configurations)}")