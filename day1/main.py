with open("day1/input.txt") as f:
    pairs = [line.strip().split() for line in f.readlines()]

left = sorted([int(pair[0]) for pair in pairs])
right = sorted([int(pair[1]) for pair in pairs])

part1 = sum([abs(l-r) for l, r in zip(left, right)])
print(part1)

from collections import Counter

counter = Counter(right)

part2 = sum(l * counter[l] for l in left)
print(part2)



