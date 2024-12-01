import typer

@typer.run
def main(input: typer.FileText) -> None:
    loose = 0
    draw = 3
    win = 6

    rock = 1
    paper = 2
    scissor = 3

    scores = {
        # A, X = rock
        # B, Y = paper
        # C, Z = scissor
        "A X": rock + draw,
        "A Y": paper + win,
        "A Z": scissor + loose,
        "B X": rock + loose,
        "B Y": paper + draw,
        "B Z": scissor + win,
        "C X": rock + win,
        "C Y": paper + loose,
        "C Z": scissor + draw,
    }

    print(sum(scores[line.strip()] for line in input.readlines()))

    return None
