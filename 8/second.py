from pathlib import Path
import sys



def _setify(codes):
    return [frozenset(code) for code in codes]

def _find(codes, length, check=lambda code: True):
    matches = [code for code in codes if len(code) == length and check(code)]
    assert len(matches) == 1
    return matches[0]


class SignalPatterns:
    def __init__(self, input_patterns):
        patterns = _setify(input_patterns)

        one = _find(patterns, 2)
        four = _find(patterns, 4)
        seven = _find(patterns, 3)
        eight = _find(patterns, 7)

        three = _find(patterns, 5, lambda code: one < code)

        six = _find(patterns, 6, lambda code: not one < code)
        one_upper = one - six
        one_lower = one - one_upper

        five = _find(patterns, 5, lambda code: code != three and one_lower < code)
        two = _find(patterns, 5, lambda code: code != three and one_upper < code)

        nine = _find(patterns, 6, lambda code: four < code)
        zero = _find(patterns, 6, lambda code: code not in [six, nine])

        self._decoded = {
            zero: 0,
            one: 1,
            two: 2,
            three: 3,
            four: 4,
            five: 5,
            six: 6,
            seven: 7,
            eight: 8,
            nine: 9,
        }

    def sum_output(self, output_patterns):
        [a, b, c, d] = _setify(output_patterns)
        return (
            + self._decoded[a] * 1000
            + self._decoded[b] * 100
            + self._decoded[c] * 10
            + self._decoded[d]
        )

def parse_line(line):
    i, o = line.split(' | ')
    return i.split(), o.split()
lines = [parse_line(line) for line in Path(sys.argv[1]).read_text().strip().splitlines()]

print(sum(SignalPatterns(inputs).sum_output(outputs) for inputs, outputs in lines))
