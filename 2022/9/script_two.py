import typer


def move(pos, direction):
    x, y = pos

    if direction == "L":
        return (x - 1, y)

    if direction == "R":
        return (x + 1, y)

    if direction == "U":
        return (x, y + 1)

    if direction == "D":
        return (x, y - 1)

    raise AssertionError(direction)


def update_tail(h, t):
    h_x, h_y = h
    t_x, t_y = t
    d_x = t_x - h_x
    d_y = h_y - t_y

    if abs(d_x) <= 1 and abs(d_y) <= 1:
        return t

    if d_y > 0:
        t = move(t, "U")

    if d_y < 0:
        t = move(t, "D")

    if d_x > 0:
        t = move(t, "L")

    if d_x < 0:
        t = move(t, "R")

    return t


def print_board(size, rope, seen):
    for y in reversed(range(0, size)):
        print("".join(marker((x, y), rope, seen) for x in range(0, size)))
    print()


def marker(pos, rope, seen):
    for idx, rope_pos in enumerate(rope):
        if rope_pos == pos:
            return str(idx).replace("0", "H")
    if pos in seen:
        return "#"
    return "."


@typer.run
def main(input: typer.FileText) -> None:
    lines = [line.strip().split() for line in input.readlines()]
    moves = [(direction, int(steps)) for direction, steps in lines]
    rope = [(0, 0)] * 10
    seen = set()

    for direction, steps in moves:
        for _ in range(steps):
            print(f"--- {direction} ---")

            rope[0] = move(rope[0], direction)

            for idx in range(len(rope) - 1):
                rope[idx + 1] = update_tail(rope[idx], rope[idx + 1])

            seen.add(rope[-1])
            print_board(6, rope, seen)

    print(len(seen))

    return None
