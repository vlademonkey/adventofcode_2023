import re
from collections import deque


network = dict()
instructions = deque()


# Would also work: itertools.cycle(instructions)
def next_node():
    global instructions
    next_node = instructions.popleft()
    instructions.append(next_node)
    return next_node


with open("input.txt") as fin:
    instructions.extend(i for i in fin.readline().strip())
    fin.readline()  # Blank line
    for line in fin:
        if match := re.match(r"(\w{3}) = \((\w{3}), (\w{3})\)", line):
            node, left, right = match.groups()
            network[node] = dict()
            network[node]["L"] = left
            network[node]["R"] = right

curr_node = "AAA"
steps = 0
while curr_node != "ZZZ":
    steps += 1
    curr_node = network[curr_node][next_node()]

print(steps)
