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

dish = tuple(tuple(row) for row in input_text.splitlines())


def rotate(dish: tuple[tuple[str, ...], ...]) -> tuple[tuple[str, ...], ...]:
    return tuple(
        tuple(dish[row][col] for row in reversed(range(len(dish))))
        for col in range(len(dish[0]))
    )


def tilt(dish: tuple[tuple[str, ...], ...]) -> tuple[tuple[str, ...], ...]:
    return tuple(
        tuple("#".join("".join(sorted(tuple(section))) for section in "".join(row).split("#")))
        for row in dish
    )


total_cycles = 1000000000
dishes = []
for current_index in range(total_cycles):
    for _ in range(4):
        dish = tilt(rotate(dish))

    if dish in dishes:
        start_index = dishes.index(dish)
        end_index = len(dishes)
        size = end_index - start_index
        left_cycles = total_cycles - current_index - 1
        dish = dishes[start_index + (left_cycles % size)]
        break

    dishes.append(dish)

# print('\n'.join(''.join(row) for row in dish))

total = 0
for i, row in enumerate(reversed(dish), start=1):
    total += row.count("O") * i

print("Answer:", total)
