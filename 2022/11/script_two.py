from typing import Callable
from pprint import pprint
import operator
import sys
import pathlib
import math
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


def run(rounds, limit_func):
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

    for n in range(rounds):
        for idx, monkey in enumerate(monkeys):
            # print(f"Monkey {idx}")
            while monkey.items:
                item = monkey.items.pop(0)
                # print(" look ", item)
                new_level = limit_func(monkey.operation(item))
                # print("  newlevel", new_level)
                next_monkey = (
                    monkey.if_true
                    if (new_level % monkey.test_divisble_by) == 0
                    else monkey.if_false
                )
                monkeys[next_monkey].items.append(new_level)
                monkey.throws += 1
                # print(f"  {next_monkey=} {new_level=}")

    # print(f"==== After round {rounds} =====")
    # for idx, monkey in enumerate(monkeys):
    #     print(f"Monkey {idx} inspected items {monkey.throws} times.")

    return [monkey.throws for monkey in monkeys]


expected = [
    (1, [2, 4, 3, 6]),
    (20, [99, 97, 8, 103]),
    (100, [5204, 4792, 199, 5192]),
]


divide_funcs = [f"x // {n}" for n in range(1, 100)]
mod_funcs = [f"x % {n}" for n in range(1, 1000)]
min_funcs = [f"min({n}, x)" for n in range(1, 1000001)]
min_bit_funcs = [f"min({n}, x)" for n in [0xFF, 0xFFFF, 0xFFFFFFFF, 0xFFFFFFFFFFFFFFFF]]
mod_bit_funcs = [f"x % {n}" for n in [0xFF, 0xFFFF, 0xFFFFFFFF, 0xFFFFFFFFFFFFFFFF]]
math_funcs = [
    "math.cbrt(x)",
    "math.log(x)",
    "math.log1p(x)",
    "math.log2(x)",
    "math.log10(x)",
    "math.isqrt(x)",
]
bit_funcs = [
    "x & 0xff",
    "x & 0xffff",
    "x & 0xffffffff",
    "x & 0xffffffffffffffff",
]
shifts = [f"x >> {n}" for n in range(20)]
subtracts = [f"x - {n}" for n in range(10_000)]
limit_funcs = math_funcs + divide_funcs + mod_funcs + min_funcs
limit_funcs = subtracts


for limit_func_str in limit_funcs:

    limit_func = eval(f"lambda x: ({limit_func_str})")

    print(f"func {limit_func_str}")
    success = True
    for rounds, expected_result in expected:
        result = run(rounds, limit_func)
        if result != expected_result:
            # print(f" {rounds=} noo :(")
            success = False
            break
        # else:
        # print(f" {rounds=} yay!")
    if success:
        print("!!!!!!! OMG YES !!!!!!!!!!")
        break
    print()


# a, b, *_ = sorted((monkey.throws for monkey in monkeys), reverse=True)

# pprint(a * b)
