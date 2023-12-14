from functools import cache
from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = """???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1"""

lines = input_text.splitlines()


@cache
def count_arrangements(string: str, digits: tuple[int, ...]) -> int:
    if not digits:
        return int("#" not in string)

    current, *digits = digits

    result = 0
    for start_index in range(len(string)):
        if "#" in string[:start_index]:
            break

        end_index = start_index + current
        if (
            end_index <= len(string)
            and "." not in string[start_index: end_index]
            and (end_index >= len(string) or string[end_index] != "#")
        ):
            result += count_arrangements(string[end_index + 1:], tuple(digits))

    return result


total_arrangements = 0

for i, line in enumerate(lines, start=1):
    string, digits = line.split()

    string = "?".join([string] * 5)
    digits = ",".join([digits] * 5)

    digits = tuple(int(digit) for digit in digits.split(","))

    arrangements = count_arrangements(string, digits)
    total_arrangements += arrangements

print("Answer:", total_arrangements)
