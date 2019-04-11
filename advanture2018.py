def read_file(day):
    file_template='data/input{}.txt'
    file = open(file_template.format(day))
    return file

from itertools import cycle

def inputd1(file):
    arr = list()
    for line in file:
        arr.append(int(line))
    return arr

input1 = inputd1(read_file(1))
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

print('Day1 Quiz 2')
print(seen_before(step_sum(cycle(input1))))


def inputd2(file):
    arr = list()
    for line in file:
        arr.append(line.strip())
    return arr

input2 = inputd2(read_file(2))
# print(input2)

def count_letter(boxid):
    twice = 0
    three = 0
    for c in boxid:
        if boxid.count(c) == 2:
            twice = 1
        if boxid.count(c) == 3:
            three = 1
    return twice, three

def scan_box(input):
    map2 = dict()
    map3 = dict()
    for box in input:
        two, three = count_letter(box)
        map2[box] = two
        map3[box] = three
    return map2, map3

def checksum(map):
    sum = 0
    for k in map:
        sum += map[k]
    return sum
map2, map3 = scan_box(input2)
print('Day2 quiz 1')
print(checksum(map2)*checksum(map3))    

    
def count_similar(id1, id2):
    similar = 0
    for i in range(min(len(id1), len(id2))):
        if id1[i] == id2[i]:
            similar += 1
    return similar

def find_most_similar(input):
    similar = ['', '', 0]  
    for box1 in input:
        for box2 in input[input.index(box1)+1:]:
            similar_num = count_similar(box1, box2)
            if similar_num > similar[2]:
                similar[0] = box1
                similar[1] = box2
                similar[2] = similar_num
    return similar

def find_boxid(id1, id2):
    boxid = ''
    for i in range(min(len(id1), len(id2))):
        if id1[i] == id2[i]:
            boxid += id1[i]
    return boxid

most_similar = find_most_similar(input2)
print(most_similar)
print('Day2 quiz 2')
print(find_boxid(most_similar[0], most_similar[1]))

"""
# How experts solve day2
"""
cat = ''.join
def common(A, B):
    return cat(a for a,b in zip(A, B) if a == b)
def diff(A, B):
    return sum(a != b for a, b in zip(A, B))
print(common(*[i for i in input2 if any(diff(i, x) == 1 for x in input2)]))
# The best solution is only 1 difference, but what if it does not exist?
# In the quiz, it indicates that "However, the IDs fghij and fguij differ 
# by exactly one character, the third (h and u). Those must be the correct
# boxes.

"""
day 3
"""

import re

def read_integers(input):
    arr = list()
    for text in input:
        arr.append(tuple(map(int, re.findall(r'-?\d+', text))))
    return arr

def inputd3(file):
    arr = list()
    for line in file:
        arr.append(line.strip())
    return arr

input3 = inputd3(read_file(3))
input3claims = read_integers(input3)

from collections import Counter
from itertools import product

def claimd(claims):
    C = Counter()
    for (id, x, y, w, h) in claims:
        C += Counter(product(range(x, x+w), range(y, y+h)))
    return C

def find_overlap(dic, overlap):
    num = 0
    for x in dic:
        if dic[x] >= overlap:
            num += 1
    return num
print('day3 quiz 1')
print(find_overlap(claimd(input3claims), 2))

def claimd2(claims):
    C = claimd(claims)
    for (id, x, y, w, h) in claims:
        if all(C[pos] == 1 for pos in product(range(x, x+w), range(y, y+h))):
            return id

print('day3 quiz 2')
print(claimd2(input3claims))


"""
day 4
"""
def inputd4(file):
    #arr = list()
    for line in file:
        yield line.strip()

def parse_record(text):
    text = re.sub('[][#:]', ' ', text)
    day, hour, mins, opcode, arg, *rest = text.split()
    return day, int(mins), opcode, arg

file = read_file(4)
day4data = sorted(map(parse_record, inputd4(file)))

from collections import defaultdict

def time_record(data):
    """
    return {guard: [day: [asleep_range]]}
    """
    sleep = defaultdict(lambda: defaultdict(list))  # sleep[guard][day] = [minutes ..]
    for day, mins, opcode, arg in data:
        if opcode == 'Guard':
            guard = int(arg)
        elif opcode == 'falls':
            falls = mins
        elif opcode == 'wakes':
            wakes = mins
            sleep[guard][day].extend(range(falls, wakes))
        else:
            raise ValueError
    return sleep

cleaned_data_day4 = time_record(day4data)

def sleepmost_guard(sleep):
    return max(sleep, key=lambda guard: sum(map(len, sleep[guard].values())))

def sleepmost_minute(guard, sleep):
    def times_alseep(m) : 
        return sum(m in mins for mins in sleep[guard].values())
    return max(range(60), key=times_alseep)

def result_day4_1(sleep_data):
    guard = sleepmost_guard(sleep_data)
    print(guard)
    minute = sleepmost_minute(guard, sleep_data)
    print(minute)
    return guard*minute

print('day4 quiz 1:')
print(result_day4_1(cleaned_data_day4))
