from pathlib import Path
import sys


def _find(codes, length, check=lambda code: True):
    matches = [code for code in codes if len(code) == length and check(code)]
    assert len(matches) == 1
    return matches[0]


class SignalPatterns:
    def __init__(self, inputs):
        one = _find(inputs, 2)
        four = _find(inputs, 4)
        seven = _find(inputs, 3)
        eight = _find(inputs, 7)

        three = _find(inputs, 5, lambda code: one < code)

        six = _find(inputs, 6, lambda code: not one < code)
        one_upper = one - six
        one_lower = one - one_upper

        five = _find(inputs, 5, lambda code: code != three and one_lower < code)
        two = _find(inputs, 5, lambda code: code != three and one_upper < code)

        nine = _find(inputs, 6, lambda code: four < code)
        zero = _find(inputs, 6, lambda code: code not in [six, nine])

        self._decoded = {zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9}

    def sum_output(self, outputs):
        [a, b, c, d] = outputs
        return (
            + self._decoded[a] * 1000
            + self._decoded[b] * 100
            + self._decoded[c] * 10
            + self._decoded[d]
        )

def parse_line(line):
    def setify(codes):
        return [frozenset(code) for code in codes]

    i, o = line.split(' | ')

    return setify(i.split()), setify(o.split())

lines = [parse_line(line) for line in Path(sys.argv[1]).read_text().strip().splitlines()]

print(sum(SignalPatterns(inputs).sum_output(outputs) for inputs, outputs in lines))
