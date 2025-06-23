from common.utils import get_input
from functools import reduce

input = get_input(day=22)
initial_secrets = list(map(int, input.splitlines()))

def mix(value: int, secret: int) -> int:
    return value ^ secret

def prune(value: int):
    return value % 16777216

def pipeline(secret: int) -> int:
    secret = mix(secret * 64, secret)
    secret = prune(secret)
    secret = mix(secret // 32, secret)
    secret = prune(secret)
    secret = mix(secret * 2048, secret)
    secret = prune(secret)

    return secret

def first_part() -> int:
    return sum(reduce(lambda acc, _: pipeline(acc), range(2000), secret) for secret in initial_secrets)

def second_part() -> int:
    total_bananas = dict()
    for secret in initial_secrets:
        prices = []
        for _ in range(2000 + 1): # to have 2000 differences
            prices.append(secret % 10)
            secret = pipeline(secret)
        
        diffs = [b - a for a, b in zip(prices, prices[1:])]
        seen = set()
        for sequence, price in [(tuple(diffs[i:i + 4]), prices[i + 4]) for i in range(len(prices) - 4)]:
            if sequence in seen: continue
            seen.add(sequence)
            if sequence not in total_bananas: 
                total_bananas[sequence] = 0
            total_bananas[sequence] += price
             
    return max(total_bananas.values())
    
print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")