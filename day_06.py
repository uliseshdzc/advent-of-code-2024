from common.utils import get_input

input = get_input(day=6)
grid = input.splitlines()
start = next((i, j) for i, row in enumerate(grid) for j, char in enumerate(row) if char == "^")

def first_part() -> int:
    guard = (*start, -1, 0) 
    visited = set()
    while True:
        i, j, di, dj = guard
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            return len(visited)
        if grid[i][j] == "#":
            guard = (i - di, j - dj, dj, -di)
            continue
        visited.add((i, j))
        guard = (i + di, j + dj, di, dj)

def check_for_loop(obstacle: tuple[int, int]) -> bool:
    guard = (*start, -1, 0) 
    states = set()
    while True:
        i, j, di, dj = guard
        if guard in states:
            return True
        states.add(guard)
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            return False
        if grid[i][j] == "#" or (i, j) == obstacle:
            guard = (i - di, j - dj, dj, -di)
            continue
        guard = (i + di, j + dj, di, dj)

def second_part() -> int:
    return sum(check_for_loop((i, j)) for i, row in enumerate(grid) for j, char in enumerate(row) if char != "#")

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")