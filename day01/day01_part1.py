# Advent of Code 2025 - Day 1: Secret Entrance
# Count how many times the dial lands on 0
# Dial is 0-99, starts at 50, L = subtract, R = add, wraps with % 100

data = open("input.txt").read()

position = 50
count = 0

for line in data.strip().split('\n'):
    line = line.strip()
    direction = line[0]
    distance = int(line[1:])

    if direction == 'L':
        position = (position - distance) % 100
    if direction == 'R':
        position = (position + distance) % 100

    if position == 0:
        count += 1

print(count)  # Answer: 1059
