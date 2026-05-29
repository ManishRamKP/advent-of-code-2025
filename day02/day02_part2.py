# Advent of Code 2025 - Day 2 Part 2: Gift Shop
# Find all invalid product IDs in given ranges and sum them
# Invalid product ID = a number made of some sequence of digits repeated at least twice
# e.g. 55, 111, 123123, 123123123 are all invalid

def is_invalid(n):
    s = str(n)
    length = len(s)

    for seq_len in range(1, length):    # try every possible sequence length
        if length % seq_len == 0:       # only if it divides evenly into total length
            repetitions = length // seq_len
            if repetitions >= 2:        # must repeat at least twice
                sequence = s[:seq_len]
                if sequence * repetitions == s:  # does repeating it rebuild the number?
                    return True
    return False

data = open("productID.txt").read()

total = 0

for range_str in data.strip().split(','):
    start, end = range_str.strip().split('-')
    start = int(start)
    end = int(end)

    for n in range(start, end + 1):
        if is_invalid(n):
            total += n

print(total) #24774350322
