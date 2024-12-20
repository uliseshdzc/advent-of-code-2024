from collections import deque
from itertools import combinations
from common.utils import get_input

input = get_input(day=20)
grid = [list(line) for line in input.splitlines()]
stack = deque((i, j) for i, row in enumerate(grid) for j, char in enumerate(row) if char == 'S')
path = []

while stack:
    position = i, j = stack.popleft()
    if position in path or grid[i][j] == '#': continue
    path.append(position)
    if grid[i][j] == 'E': break        
    [stack.append((i + di, j + dj)) for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]]

distances = [(abs(pi - qi) + abs(pj - qj), q - p) for (p, (pi, pj)), (q, (qi, qj)) in combinations(enumerate(path), 2)]

def first_part() -> int:
    return sum(manhattan_distance == 2 and distance_in_path - manhattan_distance >= 100 for manhattan_distance, distance_in_path in distances)

def second_part() -> int:
    return sum(manhattan_distance <= 20 and distance_in_path - manhattan_distance >= 100 for manhattan_distance, distance_in_path in distances)
    
print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")