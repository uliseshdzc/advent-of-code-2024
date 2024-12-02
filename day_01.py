import heapq
from collections import Counter
from common.utils import get_input

def first_part():
    lines = get_input(day=1).split('\n')
    l = [int(row.split()[0]) for row in lines]
    r = [int(row.split()[1]) for row in lines]
    heapq.heapify(l)
    heapq.heapify(r)

    result = 0
    while l: result += abs(heapq.heappop(l) - heapq.heappop(r))

    return result

def second_part():
    lines = get_input(day=1).split('\n')
    l = set(int(row.split()[0]) for row in lines)
    occurences = Counter(int(row.split()[1]) for row in lines)

    return sum(element * occurences[element] for element in l)

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")