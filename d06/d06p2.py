import math

times = dists = []
with open("input.txt") as fin:
    times = fin.readline().strip().split(":")[1].split()
    dists = fin.readline().strip().split(":")[1].split()

time_int = int("".join(times))
dist_int = int("".join(dists))

a = -1
b = time_int
c = -dist_int
discriminant = math.sqrt(b**2 - 4 * a * c)
x1 = math.floor((time_int + discriminant) / (2 * a))
x2 = math.ceil((time_int - discriminant) / (2 * a)) - 1

print(abs(x2 - x1))
