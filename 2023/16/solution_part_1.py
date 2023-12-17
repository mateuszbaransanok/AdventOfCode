from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = r""".|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\
# ..../.\\..
# .-.-/..|..
# .|....-|.\
# ..//.|...."""

tiles = [list(line) for line in input_text.splitlines()]

directions = {
    "left": (0, -1),
    "top": (-1, 0),
    "right": (0, 1),
    "bottom": (1, 0),
}

beams = [("right", (0, 0))]
energized_tiles = set()
seen_beams = set()

while beams:
    next_beams = []
    for direction, (y, x) in beams:
        if not (0 <= y < len(tiles) and 0 <= x < len(tiles[0])):
            continue

        if (direction, (y, x)) in seen_beams:
            continue
        else:
            seen_beams.add((direction, (y, x)))

        energized_tiles.add((y, x))
        tile = tiles[y][x]

        if tile == ".":
            yv, xv = directions[direction]
            next_beams.append((direction, (y + yv, x + xv)))
        elif tile == "/":
            direction_mapper = {
                "left": "bottom",
                "top": "right",
                "right": "top",
                "bottom": "left",
            }
            next_direction = direction_mapper[direction]
            yv, xv = directions[next_direction]
            next_beams.append((next_direction, (y + yv, x + xv)))
        elif tile == "\\":
            direction_mapper = {
                "left": "top",
                "top": "left",
                "right": "bottom",
                "bottom": "right",
            }
            next_direction = direction_mapper[direction]
            yv, xv = directions[next_direction]
            next_beams.append((next_direction, (y + yv, x + xv)))
        elif tile == "-":
            if direction in ("top", "bottom"):
                next_beams.append(("left", (y, x - 1)))
                next_beams.append(("right", (y, x + 1)))
            else:
                yv, xv = directions[direction]
                next_beams.append((direction, (y + yv, x + xv)))
        elif tile == "|":
            if direction in ("left", "right"):
                next_beams.append(("top", (y - 1, x)))
                next_beams.append(("bottom", (y + 1, x)))
            else:
                yv, xv = directions[direction]
                next_beams.append((direction, (y + yv, x + xv)))
        else:
            raise ValueError(tile)

    beams = next_beams

print("Answer:", len(energized_tiles))
