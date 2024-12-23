import networkx as nx
from networkx import find_cliques
from networkx import enumerate_all_cliques
from common.utils import get_input

input = get_input(day=23)

G = nx.Graph()
connections = [tuple(line.split('-')) for line in input.splitlines()]
[G.add_edge(a, b) for a, b in connections]

def first_part() -> int:
    return len(list(filter(
        lambda clique: len(clique) == 3 and any(node.startswith('t') for node in clique),
        enumerate_all_cliques(G)
    )))

def second_part() -> str:
    return ','.join(sorted(max(list(find_cliques(G)), key=lambda x: len(x))))

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")