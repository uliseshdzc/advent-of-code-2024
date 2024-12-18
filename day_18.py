import heapq
from common.utils import get_input

WIDTH = 71
HEIGHT = 71

input = get_input(day=18)
corrupted = [tuple(map(int, line.split(','))) for line in input.splitlines()]

def find_shortest_distance(corrupted: list[tuple[int, int]]) -> int | None:
    stack = [(0, 0, 0)]
    visited = set()

    while stack:
        distance, i, j = heapq.heappop(stack)
        if (i, j) == (HEIGHT - 1, WIDTH - 1): 
            return distance
        if (j, i) in corrupted or (i, j) in visited or 0 > i or i >= HEIGHT or 0 > j or j >= WIDTH: 
            continue
        visited.add((i, j))
        [heapq.heappush(stack, (distance + 1, i + di, j + dj)) for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]]

def first_part() -> int:
    return find_shortest_distance(corrupted[:1024])

def second_part() -> str:
    iteration = 1
    while not find_shortest_distance(corrupted[:-iteration]): iteration += 1
    return ",".join(map(str, corrupted[-iteration]))
    
print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")