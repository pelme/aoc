import typer


@typer.run
def main(input: typer.FileText) -> None:
    ops = [line.split() for line in input.readlines()]
    adds = [1] + ([0] * (len(ops) * 2))

    cycle = 0
    for op in ops:
        if op[0] == "noop":
            cycle += 1
            continue

        cycle += 2
        adds[cycle] = int(op[1])

    for row in range(6):
        result = ""
        for col in range(40):
            x = sum(adds[: row * 40 + col + 1])
            result += "#" if x - 1 <= col <= x + 1 else "."

        print(result)

    return None
