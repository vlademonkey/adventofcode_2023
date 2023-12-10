# From: https://www.reddit.com/r/adventofcode/comments/18e5ytd/2023_day_9_solutions/kclqhga/

import numpy as np
from numpy.polynomial.polynomial import Polynomial
from pathlib import Path

indata = Path("input.txt").read_text()

answer = [0, 0]
for line in indata.splitlines(keepends=False):
    y = [int(x) for x in line.split()]
    poly = Polynomial.fit(np.arange(len(y)), y, deg=len(y) - 1)
    answer[0] += round(poly(len(y)))
    answer[1] += round(poly(-1))
print("Part 1: {}\nPart 2: {}".format(*answer))
