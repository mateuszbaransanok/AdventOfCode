from pathlib import Path


input_text = Path("input.txt").read_text()

# input_text = """Time:      7  15   30
# Distance:  9  40  200"""

lines = input_text.splitlines()
times = [int(x) for x in lines[0].removeprefix("Time:").strip().split()]
distances = [int(x) for x in lines[1].removeprefix("Distance:").strip().split()]

winning_ways = []
for time, distance in zip(times, distances, strict=True):
    winning_counter = 0
    for hold_time in range(1, time):
        speed = hold_time
        left_time = time - hold_time
        boat_distance = speed * left_time
        if boat_distance > distance:
            winning_counter += 1

    winning_ways.append(winning_counter)


total = 1
for winning_way in winning_ways:
    total *= winning_way

print("Answer:", total)
