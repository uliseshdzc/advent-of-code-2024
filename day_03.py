import re
from collections import deque
from common.utils import get_input


input = get_input(day=3)

def first_part():
    return sum(int(x) * int(y) for x, y in re.findall("mul\((\d+),(\d+)\)", input))

def second_part():
    instructions = deque(
        re.findall("(?:mul\(\d+,\d+\)|do\(\)|don't\(\))", input)
    )
    result = 0
    activated = True

    while instructions:
        instruction = instructions.popleft()
        match instruction:
            case "do()":
                activated = True
            case "don't()":
                activated = False
            case _ if activated:
                x, y = re.findall("\d+", instruction)
                result += int(x) * int(y)
           
    return result

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")