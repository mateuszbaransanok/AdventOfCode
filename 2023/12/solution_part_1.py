import re
from itertools import product
from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = """???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1"""

total_arrangements = 0

for line in input_text.splitlines():
    string, digits = line.split()
    digits = tuple(int(digit) for digit in digits.split(","))

    num_arrangements = 0

    num_unknown = sum(char == "?" for char in string)
    if num_unknown:
        combinations = product(*(("#", ".") for _ in range(num_unknown)))
        for combination in combinations:
            string_comb = string
            for char in combination:
                string_comb = string_comb.replace("?", char, 1)

            string_digits = tuple(len(s) for s in re.split(r"\.+", string_comb.strip(".")))

            if string_digits == digits:
                num_arrangements += 1
    else:
        string_digits = tuple(len(s) for s in re.split(r"\.+", string.strip(".")))
        if string_digits == digits:
            num_arrangements += 1

    total_arrangements += num_arrangements


print("Answer:", total_arrangements)
