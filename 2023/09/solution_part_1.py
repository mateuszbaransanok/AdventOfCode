from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""

lines = [[int(value) for value in line.split()] for line in input_text.splitlines()]


def predict_next_value(numbers: list[int]) -> int:
    if len(numbers) <= 1 or all(num == 0 for num in numbers):
        return 0

    reduced_numbers = [y - x for x, y in zip(numbers[:-1], numbers[1:], strict=True)]

    return numbers[-1] + predict_next_value(reduced_numbers)


total = sum(predict_next_value(seq) for seq in lines)

print("Answer:", total)
