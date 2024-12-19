from functools import cache
from common.utils import get_input

input = get_input(day=19)
towels, designs = input.split('\n\n')
towels = towels.split(', ')
designs = designs.splitlines()

@cache
def patterns_count(design: str) -> int:
    if len(design) == 0: return 1
    return sum(patterns_count(design[len(towel):]) for towel in towels if design.startswith(towel))

def first_part() -> int:
    return sum(patterns_count(pattern) > 0 for pattern in designs)

def second_part() -> int:
    return sum(patterns_count(pattern) for pattern in designs)
    
print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")