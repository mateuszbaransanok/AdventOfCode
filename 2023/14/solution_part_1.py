from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = """O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#...."""

dish = [list(row) for row in input_text.splitlines()]

# tilt to north
dish_tilted = [
    [
        col[i]
        for col in [
            list("#".join("".join(sorted(list(x), reverse=True)) for x in "".join(c).split("#")))
            for c in [[row[i] for row in dish] for i in range(len(dish[0]))]
        ]
    ]
    for i in range(len(dish))
]

# print('\n'.join(''.join(row) for row in dish_tilted))


total = 0
for i, row in enumerate(reversed(dish_tilted), start=1):
    total += row.count("O") * i

print("Answer:", total)
