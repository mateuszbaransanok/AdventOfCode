from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = """#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.
#
# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#"""

patterns = input_text.split("\n\n")


def find_reflection(pattern: str) -> int:
    pattern_lines = [list(row) for row in pattern.splitlines()]

    for index in range(len(pattern_lines) - 1):
        if sum(
            pattern_lines[index - row][col] != pattern_lines[index + row + 1][col]
            for col in range(len(pattern_lines[0]))
            for row in range(min(index + 1, len(pattern_lines) - index - 1))
        ) == 1:
            return 100 * (index + 1)

    for index in range(len(pattern_lines[0]) - 1):
        if sum(
            pattern_lines[row][index - col] != pattern_lines[row][index + col + 1]
            for col in range(min(index + 1, len(pattern_lines[0]) - index - 1))
            for row in range(len(pattern_lines))
        ) == 1:
            return index + 1

    raise ValueError("There is no reflection")


total = 0

for pattern in patterns:
    total += find_reflection(pattern)

print("Answer:", total)
