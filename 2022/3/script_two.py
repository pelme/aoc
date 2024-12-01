import typer
from itertools import count
import string

# from https://docs.python.org/3/library/itertools.html
def grouper(iterable, n):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return zip(*args, strict=True)


priorities = {
    item: prio
    for item, prio in zip(string.ascii_lowercase + string.ascii_uppercase, count(1))
}


@typer.run
def main(input: typer.FileText) -> None:
    lines = [line.strip() for line in input.readlines()]

    result = 0
    for a, b, c in grouper(lines, 3):
        [common] = set(a) & set(b) & set(c)
        result += priorities[common]
    print(result)

    return None
