import copy
from common.utils import get_input

input = get_input(day=15)
original_grid, instructions = input.split('\n\n')
original_grid = [list(line) for line in original_grid.splitlines()]
instructions = list("".join(instructions.splitlines()))
start = next((i, j) for i, line in enumerate(original_grid) for j, char in enumerate(line) if char == '@')
directions = {
    '<': (0, -1),
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0)
}

def first_part() -> int:
    grid = copy.deepcopy(original_grid)
    i, j = start
    for instruction in instructions:
        di, dj = directions[instruction]
        ni, nj = di + i, dj + j

        if grid[ni][nj] == '#': 
            continue
        elif grid[ni][nj] == '.':
            grid[ni][nj] = '@'
            grid[i][j] = '.'
            i, j = ni, nj
            continue

        bi, bj = ni, nj
        while grid[bi][bj] == 'O':
            bi, bj = bi + di, bj + dj

        if grid[bi][bj] == '#': continue

        grid[bi][bj] = 'O'
        grid[i][j] = '.'
        grid[ni][nj] = '@'
        i, j = ni, nj

    return sum(100 * i + j for i, line in enumerate(grid) for j, char in enumerate(line) if char == 'O')

def second_part() -> int:
    si, sj = start
    sj *= 2
    new_objects = {
        '#': ['#', '#'],
        'O': ['[', ']'],
        '.': ['.', '.'],
        '@': ['@', '.'],
    }
    grid = [[new_char for char in line for new_char in new_objects[char]] for line in original_grid]

    for instruction in instructions:
        di, dj = directions[instruction]
        targets = [(si, sj)]
        process = True

        for i, j in targets:
            ni, nj = di + i, dj + j
            if (ni, nj) in targets: continue
            if grid[ni][nj] == '#':
                process = False
                continue
            if grid[ni][nj] == '[':
                targets.extend([(ni, nj), (ni, nj + 1)])
            if grid[ni][nj] == ']':
                targets.extend([(ni, nj), (ni, nj - 1)])

        if not process: continue

        row = [list(line) for line in grid]
        grid[si][sj] = '.'
        grid[si + di][sj + dj] = '@'
        
        for bi, bj in targets[1:]: grid[bi][bj] = "."
        for bi, bj in targets[1:]: grid[bi + di][bj + dj] = row[bi][bj]

        si += di
        sj += dj

    return sum(100 * i + j for i, line in enumerate(grid) for j, char in enumerate(line) if char == '[')

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")