from collections import deque
from common.utils import get_input

input = get_input(day=12)
grid = input.splitlines()
width = len(grid[0])
height = len(grid)

def neighbors(position: tuple[int, int]) -> list[tuple[int, int]]:
    i, j = position
    return [(i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j)]

def perimeter(region: list[tuple[int, int]]) -> int:
    return sum(neighbor not in region for position in region for neighbor in neighbors(position))

def n_corners(region: list[tuple[int, int]]) -> int:
    n_corners = 0
    for position in region:
        corner_adjacents = zip(new_neighbors := neighbors(position) + neighbors(position)[:1], new_neighbors[1:])

        for c1, c2 in corner_adjacents:
            if c1 not in region and c2 not in region: 
                n_corners += 1 # Outer corners
            c12 = (c1[0] + c2[0] - position[0], c1[1] + c2[1] - position[1])
            if c1 in region and c2 in region and c12 not in region: 
                n_corners += 1 # Inner corners

    return n_corners

def get_regions() -> list[list[tuple[int, int]]]:    
    regions = []
    visited = set()
    next_lookup = deque([(0, 0)])

    while next_lookup:
        start = si, sj = next_lookup.popleft()
        stack = deque([start])
        current_region = []
        current = grid[si][sj]

        while stack:
            position = i, j = stack.popleft()
            if not(0 <= i < height and 0 <= j < width and position not in visited):
                continue
            
            if grid[i][j] != current:
                next_lookup.append(position)
                continue

            visited.add(position)
            current_region.append(position)
            [stack.append(move) for move in neighbors(position)]

        regions.append(current_region)

    return regions  

print(f"Part 1: {sum(len(region) * perimeter(region) for region in get_regions())}")
print(f"Part 2: {sum(len(region) * n_corners(region) for region in get_regions())}")