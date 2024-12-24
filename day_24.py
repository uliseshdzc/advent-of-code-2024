from collections import deque
from common.utils import get_input

input = get_input(day=24)
values, operations = input.split("\n\n")
values = {a: bool(int(b)) for a, b in (line.split(": ") for line in values.splitlines())}
operations = [(a, operator, b, output) for a, operator, b, _, output in (line.split() for line in operations.splitlines())]
stack = deque(operations)

def first_part() -> int:
    operator_values = {"AND": "and", "OR": "or", "XOR": "^"}
    while stack:
        operation = a, operator, b, output = stack.popleft()
        if a not in values.keys() or b not in values.keys():
            stack.append(operation)
            continue
        values[output] = eval(f"{values[a]} {operator_values[operator]} {values[b]}")

    zs = list(sorted(key for key in values.keys() if key.startswith('z')))

    return sum(2 ** i if values[z] else 0 for i, z in enumerate(zs))

def create_graph() -> None:
    operator_colors = {'XOR': 'green', 'AND': 'red', 'OR': 'blue'}
    operator_values = {'XOR': '^', 'AND': '&', 'OR': '|'}
    with open("circuit.dot", 'w') as f:
        f.write("digraph {\n")
        f.write('node [fontname="Consolas", shape=box width=.5];\n')
        f.write('splines=ortho;\nrankdir="LR";\n')
        for i, (a, operator, b, output) in enumerate(operations):
            if output.startswith('z'): f.write(f'{output} [color="purple"];\n')
            f.write(f'op{i} [label="{operator_values[operator]}" color="{operator_colors[operator]}"];\n')
            f.write(f"{a} -> op{i};\n")
            f.write(f"{b} -> op{i};\n")
            f.write(f"op{i} -> {output};\n")
        f.write("}")

def second_part() -> str:
    create_graph()

    swapped = set()
    last_z = f"z{len(list(filter(lambda x: x.startswith('x'),values)))}"
    for a, operator, b, output in operations:
        if output.startswith('z') and operator != "XOR" and output != last_z: 
            swapped.add(output)

        if (
            operator == "XOR" 
            and output[0] not in ["x", "y", "z"]
            and a[0] not in ["x", "y", "z"]
            and b[0] not in ["x", "y", "z"]
        ): 
            swapped.add(output)

        if operator == "OR":
            swapped.update(
                prev_output for _, prev_operator, _, prev_output in operations
                if prev_output in [a, b] and prev_operator != "AND"
            )

        if operator == "AND":
            swapped.update(
                prev_output for prev_a, prev_operator, _, prev_output in operations
                if prev_output in [a, b] and prev_a not in ["x00", "y00"] and prev_operator == "AND"
            )              

    return ",".join(sorted(swapped))

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")