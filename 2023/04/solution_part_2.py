from pathlib import Path

lines = Path("input.txt").read_text().splitlines()

# lines = [
#     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
#     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
#     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
#     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
#     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
#     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
# ]

scratchcards = {i: 1 for i in range(1, len(lines) + 1)}

for i, line in enumerate(lines, start=1):
    card_info, number_line = line.split(":")

    winning_numbers, my_numbers = number_line.split("|")
    winning_numbers = [int(x) for x in winning_numbers.split() if x]
    my_numbers = [int(x) for x in my_numbers.split() if x]

    matches = set(winning_numbers).intersection(my_numbers)
    num_matches = len(matches)

    for j in range(i + 1, min(num_matches + i, len(scratchcards)) + 1):
        if j <= len(lines):
            scratchcards[j] += scratchcards[i]

total = sum(scratchcards.values())

print("Answer:", total)
