from common.utils import get_input

input = get_input(day=8)
lines = input.splitlines()
width, height = len(lines[0]), len(lines)
antenna_map = [(i, j, char) for i, row in enumerate(input.splitlines()) for j, char in enumerate(row) if char != "."]

def first_part() -> int:
    antinodes = set()
    for i, j, antenna in antenna_map:
        sf_antennas = [(sf_i, sf_j, sf_antenna) for sf_i, sf_j, sf_antenna in antenna_map 
                       if sf_i != i and sf_j != j and antenna == sf_antenna]
        for sf_i, sf_j, _ in sf_antennas:
            di, dj = i - sf_i, j - sf_j
            if 0 <= i + di < height and 0 <= j + dj < width: antinodes.add((i + di, j + dj))
            if 0 <= sf_i - di < height and 0 <= sf_j - dj < width: antinodes.add((sf_i - di, sf_j - dj))
            
    return len(antinodes)

def second_part() -> int:
    antinodes = set()
    for i, j, antenna in antenna_map:
        sf_antennas = [(sf_i, sf_j, sf_antenna) for sf_i, sf_j, sf_antenna in antenna_map 
                       if sf_i != i and sf_j != j and antenna == sf_antenna]
        for sf_i, sf_j, _ in sf_antennas:
            di, dj = i - sf_i, j - sf_j
            ni, nj = i, j
            while 0 <= ni < height and 0 <= nj < width:
                antinodes.add((ni, nj))
                ni += di
                nj += dj
            while 0 <= sf_i < height and 0 <= sf_j < width: 
                antinodes.add((sf_i, sf_j ))
                sf_i -= di
                sf_j -= dj
            
    return len(antinodes)

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")