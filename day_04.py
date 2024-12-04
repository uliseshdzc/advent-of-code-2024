import copy
import re
import numpy as np
from common.utils import get_input

input = get_input(day=4)
data = np.array([list(line) for line in input.splitlines()])

def data_to_str_lines(data: np.ndarray) -> list[str]:
    return [''.join(row) for row in data]

def count_xmas_both_ways(line: str) -> int:
    return len(re.findall("XMAS", line)) + len(re.findall("SAMX", line))

def first_part():
    result = 0
    for rotated_data in [data, np.rot90(data)]:
        # Look throughout the horizontal lines from both sides
        result += sum(count_xmas_both_ways(line) for line in data_to_str_lines(rotated_data))
        
        # Look throughout the diagonals from both sides (the diagonals with size < 4 are not considered)
        diagonals = [rotated_data.diagonal(-len(rotated_data) + k + 1) for k in range(3, len(rotated_data) * 2 - 4)]
        result += sum(count_xmas_both_ways(diagonal) for diagonal in data_to_str_lines(diagonals))

    return result

def get_cross_matrix(row: int, col: int) -> list[list[str]]:
    matrix = copy.copy(data[row-1:row+2, col-1:col+2])
    for i, j in [(0, 1), (1, 0), (1, 2), (2, 1)]:
        matrix[i, j] = ''

    return matrix.tolist()

def second_part():
    possibilities = [
        [['M','','S'], ['','A',''], ['M','','S']],
        [['M','','M'], ['','A',''], ['S','','S']],
        [['S','','M'], ['','A',''], ['S','','M']],
        [['S','','S'], ['','A',''], ['M','','M']],
    ]
    indices = [(i, j) for i in range(1, data.shape[0] - 1) for j in range(1, data.shape[1] - 1)]

    return sum(get_cross_matrix(*index) in possibilities for index in indices)

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")