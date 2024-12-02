from common.utils import get_input

lines = get_input(day=2).split('\n')

def is_safe(levels: list[int]):
    diffs = [first - second for (first, second) in zip(levels, levels[1:])]
    return all(1 <= diff <= 3 for diff in diffs) or all(-3 <= diff <= -1 for diff in diffs)

def first_part():
    return sum(is_safe(list(map(int, line.split()))) for line in lines)

def second_part():
    result = 0
    for levels in [list(map(int, line.split())) for line in lines]:
        if any(is_safe(levels[:i] + levels[i + 1:]) for i in range(len(levels))):
            result += 1
    return result

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")