python# Advent of Code 2025 - Day 1 Part 2: Secret Entrance
# Count every time the dial passes through or lands on 0 during any rotation
# Dial is 0-99, starts at 50, L = subtract 1 click, R = add 1 click, wraps with % 100

data = open("input.txt").read()

position = 50
count = 0

for line in data.strip().split('\n'):
    line = line.strip()
    direction = line[0]
    distance = int(line[1:])
    
    for _ in range(distance):    
        if direction == 'L':
            position = (position - 1) % 100
        if direction == 'R':
            position = (position + 1) % 100
        
        if position == 0:
            count += 1

print(count)
