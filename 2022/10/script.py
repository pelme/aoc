import typer


def strength_at(adds, ends_of_cycle_n_1):
    return sum(adds[:ends_of_cycle_n_1]) * ends_of_cycle_n_1


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

    print(
        sum(
            [
                strength_at(adds, 20),
                strength_at(adds, 60),
                strength_at(adds, 100),
                strength_at(adds, 140),
                strength_at(adds, 180),
                strength_at(adds, 220),
            ]
        )
    )

    return None
