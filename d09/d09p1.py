import numpy


def predict_next_value(values: numpy.array):
    total_sums = 0
    while not all(x == 0 for x in values):
        total_sums += values[-1]
        values = numpy.diff(values)
    return total_sums


total_sum = 0
with open("input.txt") as fin:
    for line in fin:
        values = numpy.array(line.split()).astype(int)
        total_sum += predict_next_value(values)

print(total_sum)
