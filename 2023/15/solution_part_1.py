from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

lines = input_text.split(",")


def calculate_hash(string: str) -> int:
    current_value = 0
    for char in string:
        current_value = ((current_value + ord(char)) * 17) % 256
    return current_value


total = sum(calculate_hash(line) for line in lines)

print("Answer:", total)
