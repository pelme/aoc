from pathlib import Path
import sys

class FishPopulation:
    def __init__(self, initial_fishes):
        self.counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for num in initial_fishes:
            self.counts[num] += 1

    def next_day(self):
        zeros = self.counts.pop(0)
        self.counts[6] += zeros
        self.counts.append(zeros)

    def count(self):
        return sum(count for count in self.counts)

initial_numbers = [int(x) for x in Path(sys.argv[1]).read_text().split(',')]

fish_population = FishPopulation(initial_numbers)
for _ in range(256):
    fish_population.next_day()

print(fish_population.count())
