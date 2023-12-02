from pathlib import Path

number_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

lines = Path("input.txt").read_text().splitlines()

total = 0

for line in lines:
    while True:
        # find first index of replacement
        start_index = len(line)
        number = None
        for text_number, digit_number in number_mapping.items():
            index = line.find(text_number)
            if -1 < index < start_index:
                start_index = index
                number = digit_number

        # repeat for all numbers in line
        if not number:
            break

        # replace only first letter to handle e.g. oneight, sevenine cases -> 18, 79
        line = "".join((line[:start_index], number, line[start_index + 1:]))

    numbers = "".join(char for char in line if char.isdecimal())
    total += int(numbers[0] + numbers[-1])

print("Answer:", total)
