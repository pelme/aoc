import typer


def parse_line(l):
    a, b = l.split(",")
    return parse_pair(a), parse_pair(b)


def parse_pair(s):
    lower, upper = s.split("-")
    return set(range(int(lower), int(upper) + 1))


@typer.run
def main(input: typer.FileText) -> None:
    pairs = [parse_line(line.strip()) for line in input.readlines()]
    print(sum(1 for a, b in pairs if a & b))
    return None
