position = 0
depth = 0

for line in open('input.txt', "r", encoding="utf8"):
    match line.split():
        case ('forward', x):
            position += int(x)
        case ('down', x):
            depth += int(x)
        case ('up', x):
            depth -= int(x)

print(f'{position * depth=}')
