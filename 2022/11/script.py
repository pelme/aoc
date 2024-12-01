from typing import Callable
from pprint import pprint
import operator
import sys
import pathlib

from dataclasses import dataclass

lines = [
    line.strip() for line in pathlib.Path(sys.argv[1]).read_text().splitlines() if line
]

# from https://docs.python.org/3/library/itertools.html
def grouper(iterable, n):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return zip(*args, strict=True)


@dataclass
class Monkey:
    throws: int
    items: list[int]
    operation: Callable[[int], int]
    test_divisble_by: int
    if_true: int
    if_false: int


monkeys: list[Monkey] = []


def parse_items(line):
    return [int(x) for x in line.removeprefix("Starting items: ").split(",")]


def parse_operation(line: str):
    op_str, value = line.removeprefix("Operation: new = old ").split()
    op = {
        "*": operator.mul,
        "+": operator.add,
    }[op_str]

    return lambda x: op(x, x if value == "old" else int(value))


for _, starting_items, operation, test, if_true, if_false in grouper(lines, 6):
    monkeys.append(
        Monkey(
            throws=0,
            items=parse_items(starting_items),
            operation=parse_operation(operation),
            test_divisble_by=int(test.removeprefix("Test: divisible by")),
            if_true=int(if_true.removeprefix("If true: throw to monkey ")),
            if_false=int(if_false.removeprefix("If false: throw to monkey ")),
        )
    )

for n in range(20):
    for idx, monkey in enumerate(monkeys):
        print(f"Monkey {idx}")
        while monkey.items:
            item = monkey.items.pop(0)
            print(" look ", item)
            new_level = monkey.operation(item) // 3
            print("  newlevel", new_level)
            next_monkey = (
                monkey.if_true
                if (new_level % monkey.test_divisble_by) == 0
                else monkey.if_false
            )
            monkeys[next_monkey].items.append(new_level)
            monkey.throws += 1
            print(f"  {next_monkey=} {new_level=}")

a, b, *_ = sorted((monkey.throws for monkey in monkeys), reverse=True)

pprint(a * b)
