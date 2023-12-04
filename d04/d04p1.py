sum = 0

with open("input.txt") as fin:
    for line in fin:
        nums = line.strip().split(":")[1].split("|")
        a = set(nums[0].split())
        b = set(nums[1].split())
        c = a.intersection(b)
        if c:
            sum += 2 ** (len(c) - 1)


print(sum)
