from collections import Counter

with open('input.txt', 'r', encoding='utf8') as f:
    all_inputs = [line.strip() for line in f]

assert all(len(input) == 12 for input in all_inputs)

def calculate(keeper_bit_func, inputs, bit_number):
    counter = Counter()
    for input in inputs:
        counter[input[bit_number]] += 1

    keep_bit = keeper_bit_func(counter)
    remaining = [input for input in inputs if input[bit_number] == keep_bit]

    match remaining:
        case [result]:
            return int(result, base=2)
        case _:
            return calculate(
                keeper_bit_func,
                inputs=remaining,
                bit_number=bit_number + 1,
            )

oxygen = calculate(
    keeper_bit_func=lambda counter: '1' if counter['1'] >= counter['0'] else '0',
    inputs=all_inputs,
    bit_number=0,
)

co2 = calculate(
    keeper_bit_func=lambda counter: '0' if counter['0'] <= counter['1'] else '1',
    inputs=all_inputs,
    bit_number=0,
)

print(f'{oxygen=} {co2=} {oxygen * co2=}')
