from itertools import pairwise

def triplewise(iterable):
    "Return overlapping triplets from an iterable"
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c


with open('input.txt', "r", encoding="utf8") as f:
    previous = None
    increments = 0

    for a, b, c in triplewise(f):
        current = int(a) + int(b) + int(c)

        if previous is not None:
            if current > previous:
                increments += 1
        previous = current

    print(increments)

