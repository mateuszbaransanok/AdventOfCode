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
    for star_match in re.finditer(r"\*", line):
        star_index = star_match.end()
        star_numbers = []
        for k in range(max(i - 1, 0), min(i + 2, len(lines))):
            for match in re.finditer(r"\d+", lines[k]):
                if match.start() <= star_index <= match.end() + 1:
                    number = int(match.group())
                    star_numbers.append(number)

        if len(star_numbers) == 2:
            product = 1
            for number in star_numbers:
                product *= number

            total += product

print("Answer:", total)
