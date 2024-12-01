import typer

# [M] [H]         [N]
# [S] [W]         [F]     [W] [V]
# [J] [J]         [B]     [S] [B] [F]
# [L] [F] [G]     [C]     [L] [N] [N]
# [V] [Z] [D]     [P] [W] [G] [F] [Z]
# [F] [D] [C] [S] [W] [M] [N] [H] [H]
# [N] [N] [R] [B] [Z] [R] [T] [T] [M]
# [R] [P] [W] [N] [M] [P] [R] [Q] [L]
#  1   2   3   4   5   6   7   8   9



M S J L V F N R


stacks = {
    1:"MSJLVFNR",
    2: HWJFZDNP,
    3: GDCRW,
    4: SBN,
    5: NFBCPWZM,
    6: WMRP
    7: WSLGNTR
    8:

}

@typer.run
def main(input: typer.FileText) -> None:
    s = input.read()
    return None
