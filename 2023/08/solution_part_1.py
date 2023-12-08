import itertools
from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = """RL
#
# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)"""
#
# input_text = """LLR
#
# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)"""

lines = input_text.splitlines()
instructions = list(lines[0])

mapping = {}
for line in lines[2:]:
    key, values = line.split(" = ")
    left, right = values.strip("()").split(", ")
    mapping[key] = {
        "L": left,
        "R": right,
    }

current_value = "AAA"

for steps, instruction in enumerate(itertools.cycle(instructions), start=1):
    current_value = mapping[current_value][instruction]
    if current_value == "ZZZ":
        print("Answer:", steps)
        break
