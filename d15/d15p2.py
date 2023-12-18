import re
from collections import defaultdict, namedtuple
import pprint

Mirror = namedtuple("Mirror", ["label", "focal_len"])

linepart_re = re.compile(r"(\w+)(=|-)(\d+)?")


def calc_hash(hash: str) -> int:
    total = 0
    for char in hash:
        total += ord(char)
        total *= 17
        total %= 256
    return total


with open("input.txt") as fin:
    line = fin.readline().strip()

boxes = defaultdict(list)
lineparts = line.split(",")

for linepart in lineparts:
    if match := linepart_re.match(linepart):
        label, operator, focal_len = match.groups()
        boxnum = calc_hash(label)
        # Remove mirror.
        if operator == "-":
            if boxnum in boxes:
                for mirror in boxes[boxnum]:
                    if mirror.label == label:
                        boxes[boxnum].remove(mirror)
        # Add mirror.
        elif operator == "=":
            mirror_found = False
            if boxnum in boxes:
                for idx, mirror in enumerate(boxes[boxnum]):
                    if mirror.label == label:
                        boxes[boxnum][idx] = Mirror(label, focal_len)
                        mirror_found = True
            if not mirror_found:
                boxes[boxnum].append(Mirror(label, focal_len))


pprint.pprint(boxes)

total = 0
for box_idx, box in boxes.items():
    for mir_idx, mirror in enumerate(box):
        total += (box_idx + 1) * (mir_idx + 1) * int(mirror.focal_len)

print(total)
