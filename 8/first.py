from pathlib import Path
import sys

def parse_line(line):
    i, o = line.split(' | ')
    return i.split(), o.split()

lines = [parse_line(line) for line in Path(sys.argv[1]).read_text().strip().splitlines()]

res = 0
for i, o in lines:
    for code in o:
        if len(code) in (2, 3, 4, 7):
            res += 1

print(res)
