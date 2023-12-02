from pathlib import Path

lines = Path("input.txt").read_text().splitlines()

total = 0

for line in lines:
    numbers = "".join(char for char in line if char.isdecimal())
    total += int(numbers[0] + numbers[-1])

print("Answer:", total)
