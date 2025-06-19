from common.utils import get_input

input = get_input(day=9)

def first_part() -> int:
    disk = list(map(int, list(input)))
    l, r = 0, len(disk) - 2 if len(disk) % 2 == 0 else len(disk) - 1

    result = []
    while l <= r:
        if l % 2 == 0:
            result.extend([l // 2] * disk[l])
        else:
            while disk[l] > 0:
                if disk[l] >= disk[r]: 
                    result.extend([r // 2] * disk[r])
                    disk[l] -= disk[r]
                    r -= 2
                else: 
                    result.extend([r // 2] * disk[l])
                    disk[r] -= disk[l]
                    disk[l] = 0
        l += 1

    return sum(i * value for i, value in enumerate(result))

def second_part() -> int:
    files, spaces, index = [], [], 0
    for i, count in enumerate(map(int, list(input))):
        (files, spaces)[i % 2].append(list(range(index, index := index + count)))

    for y in reversed(range(len(files))):
        for x in range(len(spaces)):
            if len(spaces[x]) >= len(files[y]) and files[y][0] > spaces[x][0]:
                files[y] = spaces[x][:len(files[y])]
                spaces[x] = spaces[x][len(files[y]):]
    return sum((i * j) for i, f in enumerate(files) for j in f)

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")