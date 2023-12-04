with open("input.txt") as fin:
    lines = fin.readlines()

cards = [1] * len(lines)

for line_idx, line in enumerate(lines):
    nums = line.strip().split(":")[1].split("|")
    a = set(nums[0].split())
    b = set(nums[1].split())
    c = a.intersection(b)
    for i in range(line_idx + 1, line_idx + len(c) + 1):
        cards[i] += cards[line_idx]

print(cards)
print(sum(cards))
