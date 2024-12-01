import typer

from itertools import product


def paths_from_tree(tree_x, tree_y, size):
    up = [(x, tree_y) for x in range(tree_x - 1, -1, -1)]
    left = [(tree_x, y) for y in range(tree_y - 1, -1, -1)]
    right = [(tree_x, y) for y in range(tree_y + 1, size)]
    down = [(x, tree_y) for x in range(tree_x + 1, size)]
    return [up] + [left] + [right] + [down]


@typer.run
def main(input: typer.FileText) -> None:
    tree_map = [list(map(int, list(line.strip()))) for line in input.readlines()]

    assert len(tree_map) == len(tree_map[0])
    size = len(tree_map)

    best_score = 0
    for x, y in product(range(size), repeat=2):
        score = 1
        for path in paths_from_tree(x, y, size):
            house_height = tree_map[x][y]

            visible = 0
            for p_x, p_y in path:
                visible += 1
                if tree_map[p_x][p_y] >= house_height:
                    break
            score *= visible

        best_score = max(best_score, score)

    print(best_score)

    return None
