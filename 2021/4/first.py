import sys
from pathlib import Path

def int_list(lst):
    return [int(x) for x in lst]

class Board:
    def __init__(self, s):
        self.rows = [int_list(line.split()) for line in s.splitlines()]

    @property
    def cols(self):
        return [
            [row[col_idx] for row in self.rows]
            for col_idx in range(5)
        ]

    def is_won(self, drawn_numbers):
        for row in self.rows:
            if all(num in drawn_numbers for num in row):
                return True

        for col in self.cols:
            if all(num in drawn_numbers for num in col):
                return True

        return False

    def sum_unmarked(self, drawn_numbers):
        return sum(
            num
            for row in self.rows
            for num in row
            if num not in drawn_numbers
        )

[numbers_to_draw_str, boards_str] = Path(sys.argv[1]).read_text().split('\n', 1)

numbers_to_draw = int_list(numbers_to_draw_str.split(','))
boards = [
    Board(board_data)
    for board_data in boards_str.strip().split('\n\n')
]

wins = {}
drawn_numbers = set()

for current_number in numbers_to_draw:
    drawn_numbers.add(current_number)

    for board in boards:
        if board not in wins and board.is_won(drawn_numbers):
            wins[board] = current_number * board.sum_unmarked(drawn_numbers)

[winner_score, *_, loser_score] = wins.values()
print(f'{winner_score=} {loser_score=}')
