import re
from pathlib import Path

lines = Path("input.txt").read_text().splitlines()

# lines = [
#     "467..114..",
#     "...*......",
#     "..35..633.",
#     "......#...",
#     "617*......",
#     ".....+.58.",
#     "..592.....",
#     "......755.",
#     "...$.*....",
#     ".664.598..",
# ]

total = 0

for i, line in enumerate(lines):
    for match in re.finditer(r"\d+", line):
        number = int(match.group())

        left = max(match.start() - 1, 0)
        right = min(match.end() + 1, len(line))
        top = max(i - 1, 0)
        bottom = min(i + 2, len(lines))

        context = ""
        for j in range(top, bottom):
            context += lines[j][left: right]

        chars = [char for char in context if not char.isdecimal() and not char == "."]

        if chars:
            total += number

print("Answer:", total)
