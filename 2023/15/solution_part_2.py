from collections import defaultdict
from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

lines = input_text.split(",")


def calculate_hash(string: str) -> int:
    current_value = 0
    for char in string:
        current_value = ((current_value + ord(char)) * 17) % 256
    return current_value


boxes = defaultdict(dict)

for line in lines:
    if "=" in line:
        key, num = line.split("=")
        boxes[calculate_hash(key)][key] = int(num)
    elif "-" in line:
        key = line.rstrip("-")
        if key in boxes[calculate_hash(key)]:
            boxes[calculate_hash(key)].pop(key)
    else:
        raise ValueError()

total = 0
for num_box, box in boxes.items():
    for num_slot, focal_length in enumerate(box.values(), start=1):
        total += (num_box + 1) * num_slot * focal_length

print("Answer:", total)
