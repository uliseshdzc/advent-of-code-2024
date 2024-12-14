from collections import Counter
import math
import re
from common.utils import get_input

lines = get_input(day=14)
WIDTH = 101
HEIGHT = 103

def first_part() -> int:
    quadrants = Counter()
    for line in lines.splitlines():
        px, py, vx, vy = list(map(int, re.findall(r"-*\d+", line)))

        for _ in range(100):
            px = (px + vx) % WIDTH
            py = (py + vy) % HEIGHT

        if px < WIDTH // 2 and py < HEIGHT // 2: quadrants[0] += 1
        if px > WIDTH // 2 and py < HEIGHT // 2: quadrants[1] += 1
        if px < WIDTH // 2 and py > HEIGHT // 2: quadrants[2] += 1
        if px > WIDTH // 2 and py > HEIGHT // 2: quadrants[3] += 1

    return math.prod(quadrants.values())

def plot(robots: list[tuple[int, int, int, int]]) -> None:
    grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for px, py, _, _ in robots: grid[py][px] = '■'

    for line in grid:
        [print(char, end='') for char in line]
        print()

def second_part() -> int:
    consecutive_robots_on_x, i = 0, 0
    robots = [list(map(int, re.findall(r"-*\d+", line))) for line in lines.splitlines()]
    while consecutive_robots_on_x < 20:
        for robot in robots:
            px, py, vx, vy = robot
            robot[0] = (px + vx) % WIDTH
            robot[1] = (py + vy) % HEIGHT

        x_index, _ = max(Counter(px for px, _, _, _ in robots).items(), key=lambda count_item: count_item[1])
        y_values = sorted([py for px, py, _, _ in robots if px == x_index])
        consecutive_robots_on_x = len([b - a for a, b in zip(y_values, y_values[1:]) if b - a == 1])
        i += 1

    plot(robots)
    return i

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")