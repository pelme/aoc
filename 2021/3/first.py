from collections import Counter

counters = [Counter() for _ in range(12)]

for line in open('input.txt', 'r', encoding='utf8'):
    line = line.strip()
    assert len(line) == 12, repr(line)

    for idx, bit in enumerate(line):
        counters[idx][bit] += 1

gamma = sum(
    1 << idx if counter['1'] > counter['0'] else 0
    for idx, counter in enumerate(reversed(counters))
)

epsilon = gamma ^ 0b111111111111
print(f'{gamma=} {epsilon=} {gamma * epsilon=}')
