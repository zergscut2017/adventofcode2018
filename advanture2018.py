def read_file(day):
    file_template='data/input{}.txt'
    file = open(file_template.format(day))
    return file

from itertools import cycle

def input(file):
    arr = list()
    for line in file:
        arr.append(int(line))
    return arr

input1 = input(read_file(1))
print('Day1 Quiz 1')
print(sum(input1))

def step_sum(inputs):
    total = 0
    for input in inputs:
        total += input
        yield total

def seen_before(items):
    seen = {0}
    for item in items:
        if item in seen:
            return item
        seen.add(item)

print('Day2 Quiz 1')
print(seen_before(step_sum(cycle(input1))))
