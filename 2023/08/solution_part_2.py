import itertools
import math
from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = """LR
#
# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""

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

current_values = [key for key in mapping if key.endswith("A")]
cycle_steps = {}

for steps, instruction in enumerate(itertools.cycle(instructions), start=1):
    current_values = [mapping[current_value][instruction] for current_value in current_values]
    for current_value in current_values:
        if current_value.endswith("Z") and current_value not in cycle_steps:
            cycle_steps[current_value] = steps

    if len(cycle_steps) == len(current_values):
        break

print("Answer:", math.lcm(*cycle_steps.values()))
