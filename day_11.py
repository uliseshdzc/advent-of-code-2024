from collections import Counter
from common.utils import get_input

input = get_input(day=11)

def blink(n: int) -> int:
    stones = Counter(map(int, input.split()))
    for _ in range(n):
        new_stones = Counter()
        for stone, count in stones.items():
            if stone == 0:
                new_stones[1] += count
            elif (length := len(str_stone := str(stone))) % 2 == 0:
                new_stones[int(str_stone[:length // 2])] += count
                new_stones[int(str_stone[length // 2:])] += count
            else:
                new_stones[stone * 2024] += count
        stones = new_stones
        
    return sum(stones.values())

print(f"Part 1: {blink(25)}")
print(f"Part 2: {blink(75)}")