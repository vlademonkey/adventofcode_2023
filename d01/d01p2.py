
import re

nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
num_re = re.compile(rf"(?=(\d|{'|'.join(nums.keys())}))")

sum = 0
with open("input.txt") as fin:
    for line in fin:
        first = last = 0
        matches = re.findall(num_re, line)
        first = int(nums.get(matches[0], matches[0]))
        last = int(nums.get(matches[-1], matches[-1]))
        print(f"{line=} {matches=} ==> {first}{last}")
        sum += int(f"{first}{last}")

print(sum)
