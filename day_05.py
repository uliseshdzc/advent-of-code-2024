from common.utils import get_input

input = get_input(day=5)

rules, pages = input.split('\n\n')
pairs = [list(map(int, rule.split('|'))) for rule in rules.splitlines()]
pages_values = [list(map(int, line.split(','))) for line in pages.splitlines()]

def after(x: int) -> set[int]: 
    return set(a for a,b in pairs if x==b)

def get_index(x: int, values: list[int]) -> int:
    return len(after(x).intersection(values))

def first_part():
    return sum(
        page_values[len(page_values) // 2] for page_values in pages_values if 
        sorted(page_values, key=lambda x: get_index(x, page_values)) == page_values
    )

def second_part():
    result = []
    for page_values in pages_values:
        sorted_page_values = sorted(page_values, key=lambda x: get_index(x, page_values))
        if sorted_page_values != page_values:
            result.append(sorted_page_values[len(sorted_page_values) // 2])

    return sum(result)

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")