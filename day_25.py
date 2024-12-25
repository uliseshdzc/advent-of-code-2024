from common.utils import get_input

def first_part() -> int:
    blocks = [block.splitlines() for block in get_input(day=25).split("\n\n")]

    locks = [block for block in blocks if all(char == '#' for char in block[0])]
    keys = [block for block in blocks if all(char == '#' for char in block[-1])]

    lock_heights = [tuple([line[i] for line in lock].count("#") - 1 for i in range(len(lock[0]))) for lock in locks]
    key_heights = [tuple([line[i] for line in key].count("#") - 1 for i in range(len(key[0]))) for key in keys] 

    pairs = set((lock_height, key_height) for lock_height in lock_heights for key_height in key_heights
                if all(lock_height[i] + key_height[i] <= 5 for i in range(len(lock_height))))

    return len(pairs)

print(f"Part 1: {first_part()}")
print(f"Part 2: {None}")