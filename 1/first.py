with open('input.txt', "r", encoding="utf8") as f:
    previous = None
    increments = 0

    for line in f:
        current = int(line)
        if previous is not None:
            if current > previous:
                increments += 1
        previous = current

    print(increments)
