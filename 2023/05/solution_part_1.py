import re
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
    def __init__(self, map_prefix: str, text: str) -> None:
        match = re.search(rf"{map_prefix} map:\n(?P<lines>(?:\d+ \d+ \d+\n?)+)", text)
        self.mappers = [
            tuple((int(val) for val in line.split()))
            for line in match["lines"].splitlines()
        ]

    def get(self, value: int) -> int:
        for start_index, start_value, length in self.mappers:
            if start_value <= value < start_value + length:
                return start_index + value - start_value
        return value


seeds = [int(x) for x in input_text.split("\n", 1)[0].removeprefix("seeds: ").split()]
seed_to_soil_map = Mapper("seed-to-soil", input_text)
soil_to_fertilizer_map = Mapper("soil-to-fertilizer", input_text)
fertilizer_to_water_map = Mapper("fertilizer-to-water", input_text)
water_to_light_map = Mapper("water-to-light", input_text)
light_to_temperature_map = Mapper("light-to-temperature", input_text)
temperature_to_humidity_map = Mapper("temperature-to-humidity", input_text)
humidity_to_location_map = Mapper("humidity-to-location", input_text)

locations = []
for seed in seeds:
    # print("seed", seed)
    soil = seed_to_soil_map.get(seed)
    # print("soil", soil)
    fertilizer = soil_to_fertilizer_map.get(soil)
    # print("fertilizer", fertilizer)
    water = fertilizer_to_water_map.get(fertilizer)
    # print("water", water)
    light = water_to_light_map.get(water)
    # print("light", light)
    temperature = light_to_temperature_map.get(light)
    # print("temperature", temperature)
    humidity = temperature_to_humidity_map.get(temperature)
    # print("humidity", humidity)
    location = humidity_to_location_map.get(humidity)
    # print("location", location)

    locations.append(location)
    # print()

# print(locations)
print("Answer:", min(locations))
