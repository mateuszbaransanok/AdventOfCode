import re
from itertools import chain
from pathlib import Path

input_text = Path("input.txt").read_text()


# input_text = """seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4"""


class Mapper:
    MIN = 0
    MAX = 1_000_000_000_000

    def __init__(self, map_prefix: str, text: str) -> None:
        match = re.search(rf"{map_prefix} map:\n(?P<lines>(?:\d+ \d+ \d+\n?)+)", text)
        lines = [tuple((int(val) for val in line.split())) for line in match["lines"].splitlines()]
        ranges = sorted(lines, key=lambda x: (x[1], x[2]))

        self.mappers = []

        current = self.MIN
        for target, source, length in ranges:
            if source > current:
                self.mappers.append((current, current, source - current))

            self.mappers.append((target, source, length))
            current = source + length

        self.mappers.append((current, current, self.MAX - current))

    def get(self, value: int, value_length: int) -> list[tuple[int, int]]:
        ranges = []
        for target, source, length in self.mappers:
            if source <= value < source + length:
                offset = value - source
                ranges.append((target + offset, min(value_length, length - offset)))
            elif source < value + value_length <= source + length:
                ranges.append((target, value + value_length - source))
            elif value < source and source + length < value + value_length:
                ranges.append((target, length))
        return ranges

    def map(self, values: list[tuple[int, int]]) -> list[tuple[int, int]]:
        return sorted(chain(*(self.get(value, value_length) for value, value_length in values)))


seeds_ranges = [int(x) for x in input_text.split("\n", 1)[0].removeprefix("seeds: ").split()]
seed_to_soil_map = Mapper("seed-to-soil", input_text)
soil_to_fertilizer_map = Mapper("soil-to-fertilizer", input_text)
fertilizer_to_water_map = Mapper("fertilizer-to-water", input_text)
water_to_light_map = Mapper("water-to-light", input_text)
light_to_temperature_map = Mapper("light-to-temperature", input_text)
temperature_to_humidity_map = Mapper("temperature-to-humidity", input_text)
humidity_to_location_map = Mapper("humidity-to-location", input_text)

seeds = list(zip(seeds_ranges[::2], seeds_ranges[1::2], strict=True))
soils = seed_to_soil_map.map(seeds)
fertilizers = soil_to_fertilizer_map.map(soils)
waters = fertilizer_to_water_map.map(fertilizers)
lights = water_to_light_map.map(waters)
temperatures = light_to_temperature_map.map(lights)
humidities = temperature_to_humidity_map.map(temperatures)
locations = humidity_to_location_map.map(humidities)

print("Answer:", min(x[0] for x in locations))
