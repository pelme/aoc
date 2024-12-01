import typer
from itertools import count
import string


priorities = {
    item: prio
    for item, prio in zip(string.ascii_lowercase + string.ascii_uppercase, count(1))
}


@typer.run
def main(input: typer.FileText) -> None:

    result = 0
    for raw_line in input.readlines():
        line = raw_line.strip()
        middle = len(line) // 2
        [common] = set(line[:middle]) & set(line[middle:])
        result += priorities[common]
    print(result)

    return None
