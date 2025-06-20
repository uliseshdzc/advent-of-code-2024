from collections import deque
from common.utils import get_input
import heapq

input = get_input(day=16)

grid = [list(line) for line in input.splitlines()]
start = next((i, j) for i, row in enumerate(grid) for j, char in enumerate(row) if char == 'S')

def first_part() -> int:
    stack = [(0, start, (0, 1))]
    seen = set()

    while stack: 
        score, (i, j), (di, dj) = heapq.heappop(stack)  

        if grid[i][j] == 'E':
            return score

        if ((i, j), (di, dj)) in seen:
            continue

        if grid[i][j] == '#':
            continue
        
        seen.add(((i, j), (di, dj)))
        heapq.heappush(stack, (score + 1, (i + di, j + dj), (di, dj)))
        heapq.heappush(stack, (score + 1001, (i - dj, j + di), (-dj, di)))
        heapq.heappush(stack, (score + 1001, (i + dj, j - di), (dj, -di)))

def second_part() -> int:
    stack = [(0, start, (0, 1), None)]
    best_record = float("inf")
    lowest_records = {(start, (0, 1)): 0}
    backtrack = dict()
    end_positions = set()

    while stack: 
        record, (i, j), (di, dj), previous = heapq.heappop(stack)  
        current_position = ((i, j), (di, dj))

        if record > best_record: 
            continue

        if grid[i][j] == 'E':
            best_record = record
            end_positions.add(current_position)

        if grid[i][j] == '#':
            continue
                
        if record > lowest_records.get(current_position, float("inf")):
            continue        

        if current_position not in backtrack.keys(): 
            backtrack[current_position] = set()
        backtrack[current_position].add(previous)
        lowest_records[current_position] = record
                        
        heapq.heappush(stack, (record + 1, (i + di, j + dj), (di, dj), current_position))
        heapq.heappush(stack, (record + 1001, (i - dj, j + di), (-dj, di), current_position))
        heapq.heappush(stack, (record + 1001, (i + dj, j - di), (dj, -di), current_position))
        
    positions = deque(end_positions)
    seen_positions = set()
    
    while positions:
        current_position = positions.popleft()
        for previous_position in backtrack.get(current_position, []):
            if previous_position in seen_positions:
                continue
            seen_positions.add(previous_position)
            positions.append(previous_position)
        
    return len({p[0] for p in seen_positions if p}) + 1

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")