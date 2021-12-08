from itertools import repeat
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Coordinate:
    x: int
    y: int

    @classmethod
    def parse(cls, input_coordinate):
        x, y = input_coordinate.split(',')
        return cls(int(x), int(y))

@dataclass(frozen=True, slots=True)
class Line:
    start: tuple[int, int]
    end: tuple[int, int]

    @classmethod
    def parse(cls, input_line):
        a, b = input_line.split(' -> ')
        return cls(Coordinate.parse(a), Coordinate.parse(b))

    def points(self):
        if self.start.x == self.end.x:
            yield from zip(
                repeat(self.start.x),
                range(min(self.start.y, self.end.y), max(self.start.y, self.end.y) + 1),
            )

        elif self.start.y == self.end.y:
            yield from zip(
                range(min(self.start.x, self.end.x), max(self.start.x, self.end.x) + 1),
                repeat(self.start.y)
            )

        else:
            left = self.start if self.start.x <= self.end.x else self.end
            right = self.end if self.start.x <= self.end.x else self.start

            delta_y = 1 if left.y <= right.y else -1

            yield from zip(
                range(left.x, right.x + 1),
                range(left.y, right.y + delta_y, delta_y),
            )


class Diagram:
    def __init__(self):
        self._covered = Counter()

    def add_point(self, point):
        self._covered[point] += 1

    def count_overlaps(self):
        return sum(1 for count in self._covered.values() if count >= 2)


lines = [
    Line.parse(x)
    for x in Path(sys.argv[1]).read_text().splitlines()
]

diagram = Diagram()
for line in lines:
    for point in line.points():
        diagram.add_point(point)

print(diagram.count_overlaps())
