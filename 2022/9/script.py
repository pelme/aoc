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


def update(h, t, direction):
    h = move(h, direction)
    h_x, h_y = h
    t_x, t_y = t
    d_x = t_x - h_x
    d_y = h_y - t_y

    if abs(d_x) <= 1 and abs(d_y) <= 1:
        return h, t

    if d_y > 0:
        t = move(t, "U")

    if d_y < 0:
        t = move(t, "D")

    if d_x > 0:
        t = move(t, "L")

    if d_x < 0:
        t = move(t, "R")

    return h, t


def print_board(size, head, tail, seen):
    for y in reversed(range(0, size)):
        print("".join(marker((x, y), head, tail, seen) for x in range(0, size)))
    print()


def marker(pos, head, tail, seen):
    if pos == head == tail:
        return "X"

    if pos == head:
        return "H"

    if pos == tail:
        return "T"

    if pos in seen:
        return "#"
    return "."


@typer.run
def main(input: typer.FileText) -> None:
    lines = [line.strip().split() for line in input.readlines()]
    moves = [(move, int(steps)) for move, steps in lines]
    head = tail = (0, 0)
    seen = set()

    for move, steps in moves:
        for _ in range(steps):
            print(f"--- {move} ---")
            head, tail = update(head, tail, move)
            seen.add(tail)
            print_board(6, head, tail, seen)

    print(len(seen))

    return None
