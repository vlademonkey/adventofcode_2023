# From: https://www.reddit.com/r/adventofcode/comments/18e5ytd/2023_day_9_solutions/kclqhga/
import numpy as np
from numpy.polynomial.polynomial import Polynomial

with open("input.txt") as fin:
    indata = fin.read()

answer = [0, 0]
for line in indata.splitlines(keepends=False):
    y = [int(x) for x in line.split()]
    poly = Polynomial.fit(np.arange(len(y)), y, deg=len(y) - 1)
    answer[0] += round(poly(len(y)))
    answer[1] += round(poly(-1))
print("Part 1: {}\nPart 2: {}".format(*answer))

# From: https://www.reddit.com/r/adventofcode/comments/18e5ytd/2023_day_9_solutions/kco6wzm/
print(abs(sum(np.diff(np.loadtxt("input.txt", int), n=21, prepend=0, append=0))[::-1]))
