from collections.abc import Iterable
from heapq import heappop, heappush
from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = r"""2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533"""


class City:
    def __init__(
        self,
        blocks: list[list[int]],
    ) -> None:
        self.blocks = blocks
        self.height = len(blocks)
        self.weight = len(blocks[0])

    @staticmethod
    def _get_path(
        parents: dict[tuple, tuple | None],
        parent: tuple[tuple[int, int], int, tuple | None],
    ) -> list[tuple[int, int]]:
        path = []
        while parent is not None:
            coords, _, direction = parent
            path.append((coords, direction))
            parent = parents[parent]

        return list(reversed(path))

    def get_next_blocks(
        self,
        parent: tuple[tuple[int, int], int, tuple | None],
    ) -> Iterable[tuple[tuple[int, int], int, tuple | None]]:
        (parent_y, parent_x), parent_value, direction = parent
        if direction:
            dy, dx = direction

            # keep straight
            if (
                parent_value < 3
                and 0 <= parent_y + dy < self.height
                and 0 <= parent_x + dx < self.weight
            ):
                yield (parent_y + dy, parent_x + dx), parent_value + 1, (dy, dx)

            # turn left or right
            for dy, dx in (-dx, dy), (dx, -dy):
                if 0 <= parent_y + dy < self.height and 0 <= parent_x + dx < self.weight:
                    yield (parent_y + dy, parent_x + dx), 1, (dy, dx)
        else:
            # go every possible direction
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                if 0 <= parent_y + dy < self.height and 0 <= parent_x + dx < self.weight:
                    yield (parent_y + dy, parent_x + dx), 1, (dy, dx)

    def find_shortest_path(
        self,
        src: tuple[int, int],
        dst: tuple[int, int],
    ) -> tuple[int, list[tuple[int, int]], list[tuple[int, int]]] | None:
        start_node = (src, 0, None)
        costs = {start_node: 0}
        queue = [(0, start_node)]
        parents = {start_node: None}

        while queue:
            parent_cost, parent = heappop(queue)
            parent_coords, _, _ = parent

            if parent_coords == dst:
                path, directions = zip(*self._get_path(parents, parent))
                return parent_cost, path, directions

            for child in self.get_next_blocks(parent):
                (child_y, child_x), _, _ = child
                child_cost = parent_cost + self.blocks[child_y][child_x]

                if child not in costs or child_cost < costs[child]:
                    heappush(queue, (child_cost, child))
                    costs[child] = child_cost
                    parents[child] = parent

    def print_path(
        self,
        path: list[tuple[int, int]],
        directions: list[tuple[int, int]],
    ) -> None:
        direction_mapper = {
            (0, -1): "<",
            (-1, 0): "^",
            (0, 1): ">",
            (1, 0): "v",
            None: "#",
        }
        coords_to_direction = dict(zip(path, directions, strict=True))
        for y in range(len(self.blocks)):
            for x in range(len(self.blocks[0])):
                if (y, x) in coords_to_direction:
                    print(direction_mapper[coords_to_direction[(y, x)]], end="")
                else:
                    print(self.blocks[y][x], end="")
            print()


city = City([[int(block) for block in line] for line in input_text.splitlines()])
result = city.find_shortest_path(
    src=(0, 0),
    dst=(len(city.blocks) - 1, len(city.blocks[0]) - 1),
)
if result:
    cost, path, directions = result
    # city.print_path(path, directions)
    print("Answer:", cost)
