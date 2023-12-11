from collections import defaultdict
from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#....."""

space_scale = 1000000

universe = [[cell for cell in row] for row in input_text.splitlines()]

# squeeze universe
space_rows = defaultdict(int)
squeezed_rows = []
prev_space_index = -2
for i, row in enumerate(universe):
    if set(row) == {"."}:
        if i - 1 == prev_space_index:
            space_rows[len(squeezed_rows) - 1] += 1
        else:
            squeezed_rows.append(row)
            space_rows[len(squeezed_rows) - 1] = 1

        prev_space_index = i
    else:
        squeezed_rows.append(row)

space_cols = defaultdict(int)
squeezed_universe = [[] for _ in range(len(squeezed_rows))]
prev_space_index = -2
for i in range(len(squeezed_rows[0])):
    col = [row[i] for row in squeezed_rows]

    if set(col) == {"."}:
        if i - 1 == prev_space_index:
            space_cols[len(squeezed_universe[0]) - 1] += 1
        else:
            for row, cell in zip(squeezed_universe, col, strict=True):
                row.append(cell)

            space_cols[len(squeezed_universe[0]) - 1] = 1

        prev_space_index = i
    else:
        for row, cell in zip(squeezed_universe, col, strict=True):
            row.append(cell)

# print('\n'.join(''.join(row) for row in squeezed_universe))

# find galaxies
galaxies = []
for h, row in enumerate(squeezed_universe):
    for w, cell in enumerate(row):
        if cell == "#":
            galaxies.append((h, w))

# calculate distances
total_distances = 0
pairs = set()
for h1, w1 in galaxies:
    for h2, w2 in galaxies:
        if h1 == h2 and w1 == w2:
            continue

        if ((h1, w1), (h2, w2)) in pairs or ((h2, w2), (h1, w1)) in pairs:
            continue

        pairs.add(((h1, w1), (h2, w2)))

        total_distances += abs(h2 - h1) + abs(w2 - w1)

        for space, size in space_rows.items():
            if h1 < space < h2 or h1 > space > h2:
                total_distances += size * space_scale - 1

        for space, size in space_cols.items():
            if w1 < space < w2 or w1 > space > w2:
                total_distances += size * space_scale - 1

print("Answer:", total_distances)
