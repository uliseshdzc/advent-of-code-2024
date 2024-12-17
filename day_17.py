import re
from common.utils import get_input

input = get_input(day=17)
a, b, c, *program = map(int, re.findall(r"\d+", input))

def run_program(a: int, b: int = 0, c: int = 0) -> list[int]:
    ip, output = 0, []
    while ip < len(program):
        combo = {0:0, 1:1, 2:2, 3:3, 4:a, 5:b, 6:c}
        match program[ip], program[ip + 1]:
            case 0, operand: a //= 2 ** combo[operand]
            case 1, operand: b ^= operand
            case 2, operand: b = combo[operand] % 8
            case 3, operand: ip = (operand - 2) if a != 0 else ip
            case 4, operand: b ^= c
            case 5, operand: output.append(combo[operand] % 8)
            case 6, operand: b = a // 2 ** combo[operand]
            case 7, operand: c = a // 2 ** combo[operand]
        ip += 2

    return output

def first_part() -> str:    
    return ",".join(map(str, run_program(a, b, c)))

def second_part(a: int = 0, index: int = len(program) - 1) -> int | None:
    if index < 0: return a

    for i in range(8):
        a_to_test = a * 8 + i
        if run_program(a_to_test)[0] == program[index] and (result := second_part(a_to_test, index - 1)):
            return result
    
print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")