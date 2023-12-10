from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = """.....
# .S-7.
# .|.|.
# .L-J.
# ....."""

direction_mapper = {
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
    ]
}

board = []
start_coords = None

for h, line in enumerate(input_text.splitlines()):
    row = []
    for w, cell in enumerate(line):
        row.append(cell)
        if cell == "S":
            start_coords = (h, w)

    board.append(row)


def get_next_coords_and_direction(
    coords: tuple[int, int],
    direction: str,
) -> tuple[tuple[int, int], str] | tuple[None, None]:
    h_curr, w_curr = coords
    h_diff, w_diff = direction_to_coords[direction]
    h_next, w_next = h_curr + h_diff, w_curr + w_diff

    if not 0 <= h_next < len(board) or not 0 <= w_next < len(board[h_next]):
        return None, None

    next_direction = cell_to_direction[board[h_next][w_next]].get(direction_mapper[direction])

    if not next_direction:
        return None, None

    return (h_next, w_next), next_direction


seen_coords = [start_coords]

next_coords_and_directions = []
for direction in direction_mapper.keys():
    next_coords, next_direction = get_next_coords_and_direction(start_coords, direction)
    if next_coords and next_coords not in seen_coords:
        next_coords_and_directions.append((next_coords, next_direction))
        seen_coords.append(next_coords)

num_steps = 0
while next_coords_and_directions:
    new_coords_and_directions = []

    for coords, direction in next_coords_and_directions:
        next_coords, next_direction = get_next_coords_and_direction(coords, direction)
        if next_coords and next_coords not in seen_coords:
            new_coords_and_directions.append((next_coords, next_direction))
            seen_coords.append(next_coords)

    next_coords_and_directions = new_coords_and_directions
    num_steps += 1

print("Answer:", num_steps)
