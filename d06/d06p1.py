import operator
from functools import reduce

final_list = []
times = dists = []
with open("input.txt") as fin:
    times = [int(x) for x in fin.readline().strip().split(":")[1].split()]
    dists = [int(x) for x in fin.readline().strip().split(":")[1].split()]

for idx, time in enumerate(times):
    num_tests_passed = 0
    for test_time in range(time + 1):
        distance = test_time * (time - test_time)
        print(f"{test_time=} {distance=}")
        if distance > dists[idx]:
            num_tests_passed += 1
    final_list.append(num_tests_passed)

print(final_list)
print(reduce(operator.mul, final_list))
