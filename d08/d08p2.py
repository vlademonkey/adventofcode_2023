import re
from collections import deque
import itertools
import math


network = dict()
instructions = deque()
start_nodes = []
end_nodes = []

with open("input.txt") as fin:
    instructions.extend(i for i in fin.readline().strip())
    fin.readline()  # Blank line
    for line in fin:
        if match := re.match(r"(\w{3}) = \((\w{3}), (\w{3})\)", line):
            node, left, right = match.groups()
            network[node] = dict()
            network[node]["L"] = left
            network[node]["R"] = right
            if node.endswith("A"):
                start_nodes.append(node)
            if node.endswith("Z"):
                end_nodes.append(node)

step_counts = []
for start_node in start_nodes:
    inst = itertools.cycle(instructions.copy())
    curr_node = start_node
    curr_steps = 0
    while curr_node not in end_nodes:
        curr_steps += 1
        curr_node = network[curr_node][next(inst)]
    step_counts.append(curr_steps)

print(math.lcm(*step_counts))
