def calc_hash(hash: str) -> int:
    total = 0
    for char in hash:
        total += ord(char)
        total *= 17
        total %= 256
    return total


with open("input.txt") as fin:
    line = fin.readline().strip()

lineparts = line.split(",")
total = 0
for linepart in lineparts:
    total += calc_hash(linepart)

print(total)
