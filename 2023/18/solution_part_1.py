from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = r"""R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)"""

lines = input_text.splitlines()

direction_mapper = {
    "L": (0, -1),
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
}

y, x = 0, 0
coords = [(y, x)]
for line in lines:
    direction, length, color = line.split()
    length = int(length)
    dy, dx = direction_mapper[direction]
    for _ in range(length):
        y, x = y + dy, x + dx
        coords.append((y, x))


def calculate_polygon_area_with_border(coords: list[tuple[int, int]]) -> float:
    h, w = zip(*coords)
    area = 0.5 * abs(sum(h[i] * w[i - 1] - h[i - 1] * w[i] for i in range(len(coords))))
    return int(area + len(coords) / 2 + 1)


print("Answer:", calculate_polygon_area_with_border(coords))
