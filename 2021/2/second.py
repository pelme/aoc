from ast import Assert


position = 0
depth = 0
aim = 0

for line in open('input.txt', "r", encoding="utf8"):
    match line.split():
        case ('forward', x):
            position += int(x)
            depth += aim * int(x)
        case ('down', x):
            aim += int(x)
        case ('up', x):
            aim -= int(x)
        case _:
            raise AssertionError(line)


print(f'{position * depth=}')
