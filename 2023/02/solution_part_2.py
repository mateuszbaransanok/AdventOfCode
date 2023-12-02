from collections import defaultdict
from pathlib import Path

lines = Path("input.txt").read_text().splitlines()

total = 0

for line in lines:
    _, game_sets = line.split(":")

    # get minimum number of cubes
    game_bag = defaultdict(int)
    for game_set in game_sets.split(";"):
        for game_cube in game_set.split(","):
            number, color = game_cube.strip().split(" ")
            game_bag[color] = max(int(number), game_bag[color])

    # calculate power of sets
    power = 1
    for color, value in game_bag.items():
        power *= game_bag[color]

    total += power

print("Answer:", total)
