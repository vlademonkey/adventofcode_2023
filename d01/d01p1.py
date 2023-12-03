
import re

sum = 0
with open("input.txt") as fin:
    for line in fin:
        first = last = 0
        if match := re.search(r"^[^\d]*(\d)", line):
            first = int(match.group(1))
        if match := re.search(r"(\d)[^\d]*$", line):
            last = int(match.group(1))
        sum += int(f"{first}{last}")

print(sum)
