from collections import defaultdict
from pathlib import Path

lines = Path("input.txt").read_text().splitlines()

bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

total = 0

for line in lines:
    game_info, game_sets = line.split(":")
    game_number = int(game_info.split(" ")[1])

    # get minimum number of cubes
    game_bag = defaultdict(int)
    for game_set in game_sets.split(";"):
        for game_cube in game_set.split(","):
            number, color = game_cube.strip().split(" ")
            game_bag[color] = max(int(number), game_bag[color])

    # check if game is possible
    is_possible = True
    for color, value in bag.items():
        if game_bag[color] > value:
            is_possible = False
            break

    if is_possible:
        total += game_number

print("Answer:", total)
