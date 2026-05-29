# Advent of Code 2025 - Day 2 Part 1: Gift Shop
# Find all invalid IDs in given ranges and sum them
# Invalid ID = a number made of some sequence of digits repeated twice
# e.g. 55, 6464, 123123 are invalid

def is_invalid(n):
    s = str(n)
    if len(s) % 2 != 0:        # odd length can never be a repeated sequence
        return False
    half = len(s) // 2
    first_half = s[:half]
    second_half = s[half:]
    return first_half == second_half

data = open("productID.txt").read()

total = 0

for range_str in data.strip().split(','):
    start, end = range_str.strip().split('-')
    start = int(start)
    end = int(end)

    for n in range(start, end + 1):
        if is_invalid(n):
            total += n

print(total)  # Answer: 12850231731
