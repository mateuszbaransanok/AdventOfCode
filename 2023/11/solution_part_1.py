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

universe = [[cell for cell in row] for row in input_text.splitlines()]

# expand universe
expanded_rows = []
for row in universe:
    expanded_rows.append(row)
    if set(row) == {"."}:
        expanded_rows.append(row)


expanded_universe = [[] for _ in range(len(expanded_rows))]
for index in range(len(expanded_rows[0])):
    col = [row[index] for row in expanded_rows]

    for row, cell in zip(expanded_universe, col, strict=True):
        row.append(cell)

    if set(col) == {"."}:
        for row, cell in zip(expanded_universe, col, strict=True):
            row.append(cell)

# print('\n'.join(''.join(row) for row in expanded_universe))

# find galaxies
galaxies = []
for h, row in enumerate(expanded_universe):
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

print("Answer:", total_distances)
