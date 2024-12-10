from collections import deque
from common.utils import get_input

input = get_input(day=10)
grid = input.splitlines()
starting_points = [(int(i), int(j)) for i, row in enumerate(grid) for j, char in enumerate(row) if char == '0']

def get_score(i, j, all_trailheads=False):
    score = 0
    visited = set()
    stack = deque([(i, j, -1)])
    while stack:
        i, j, last_value = stack.popleft()
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and int(grid[i][j]) - 1 == int(last_value) and (i, j) not in visited:
            if not all_trailheads: visited.add((i, j))
            if grid[i][j] == '9': 
                score += 1
                continue
            stack.extend([(i + 1, j, grid[i][j]), (i - 1, j, grid[i][j]), (i, j + 1, grid[i][j]), (i, j - 1, grid[i][j])])

    return score

def first_part() -> int:
    return sum(get_score(*starting_point) for starting_point in starting_points)

def second_part() -> int:
    return sum(get_score(*starting_point, all_trailheads=True) for starting_point in starting_points)

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")