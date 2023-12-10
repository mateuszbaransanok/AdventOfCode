from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = """...........
# .S-------7.
# .|F-----7|.
# .||.....||.
# .||.....||.
# .|L-7.F-J|.
# .|..|.|..|.
# .L--J.L--J.
# ..........."""

# input_text = """..........
# .S------7.
# .|F----7|.
# .||....||.
# .||....||.
# .|L-7F-J|.
# .|..||..|.
# .L--JL--J.
# .........."""

# input_text = """.F----7F7F7F7F-7....
# .|F--7||||||||FJ....
# .||.FJ||||||||L7....
# FJL7L7LJLJ||LJ.L-7..
# L--J.L7...LJS7F-7L7.
# ....F-J..F7FJ|L7L7L7
# ....L7.F7||L7|.L7L7|
# .....|FJLJ|FJ|F7|.LJ
# ....FJL-7.||.||||...
# ....L---J.LJ.LJLJ..."""

lines = input_text.splitlines()

direction_proxy = {
    "north": "south",
    "south": "north",
    "east": "west",
    "west": "east",
}

direction_to_coords = {
    "north": (-1, 0),
    "south": (1, 0),
    "east": (0, 1),
    "west": (0, -1),
}

cell_to_direction = {
    cell: {
        direction_in: direction_out,
        direction_out: direction_in,
    }
    for cell, direction_in, direction_out in [
        ("|", "north", "south"),
        ("-", "east", "west"),
        ("L", "north", "east"),
        ("J", "north", "west"),
        ("7", "south", "west"),
        ("F", "south", "east"),
        ("S", None, None),
        (".", None, None),
    ]
}

board = []
start_coords = None

for h, line in enumerate(lines):
    row = []
    for w, cell in enumerate(line):
        row.append(cell)
        if cell == "S":
            start_coords = (h, w)

    board.append(row)


def get_next_coords_and_direction(
    coords: tuple[int, int],
    direction: str,
) -> tuple[tuple[int, int] | None, str | None]:
    h_curr, w_curr = coords
    h_diff, w_diff = direction_to_coords[direction]
    h_next, w_next = h_curr + h_diff, w_curr + w_diff

    if not 0 <= h_next < len(board) or not 0 <= w_next < len(board[h_next]):
        return None, None

    next_direction = cell_to_direction[board[h_next][w_next]].get(direction_proxy[direction])

    if not next_direction:
        return (h_next, w_next), None

    return (h_next, w_next), next_direction


seen_coords = [start_coords]
start_coords_and_directions = [
    get_next_coords_and_direction(start_coords, direction)
    for direction in direction_proxy.keys()
]
start_coords_and_directions = [
    (coords, direction)
    for coords, direction in start_coords_and_directions
    if direction
]
(next_h, next_w), next_direction = next(iter(start_coords_and_directions))

while board[next_h][next_w] != "S":
    seen_coords.append((next_h, next_w))
    (next_h, next_w), next_direction = get_next_coords_and_direction((next_h, next_w),
                                                                     next_direction)


def calculate_polygon_area_without_border(coords) -> float:
    h, w = zip(*coords)
    area = 0.5 * abs(sum(h[i] * w[i - 1] - h[i - 1] * w[i] for i in range(len(coords))))
    return int(area - len(coords) / 2 + 1)


print("Answer:", calculate_polygon_area_without_border(seen_coords))
