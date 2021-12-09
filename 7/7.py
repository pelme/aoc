from pathlib import Path
import sys

positions = [int(x) for x in Path(sys.argv[1]).read_text().split(',')]


def cost_part1(current, target):
    return abs(current - target)


def cost_part2(current, target):
    # https://en.wikipedia.org/wiki/Arithmetic_progression
    steps = abs(current - target)
    return steps * (1 + steps) // 2

cost_func = {'part1': cost_part1, 'part2': cost_part2}[sys.argv[2]]

result = min(
    sum(cost_func(position, target) for position in positions)
    for target in range(min(positions), max(positions) + 1)
)

print(result)
