from math import factorial

line = input()
line = line.split(' ')
N = int(line[0])
M = int(line[1])
pairs = {}
connects_to = {}
for i in range(M):
    line = input()
    line = line.split()
    inp = int(line[0])
    out = int(line[1])
    try:
        if out not in connects_to[inp]:
            connects_to[int(inp)].append(int(out))
    except KeyError:
        connects_to[int(inp)] = []
        connects_to[int(inp)].append(int(out))
    try:
        if inp not in connects_to[int(out)]:
            connects_to[int(out)].append(int(inp))
    except KeyError:
        connects_to[int(out)] = []
        connects_to[int(out)].append(int(inp))


max_pairs = 0
num_pairs = 0
for input in connects_to:
    branches = []
    for connection in connects_to[input]:
        num_pairs = len(connects_to[input])
        n = len(connects_to[input])
        combinations = 0
        if n > 1:
            combinations = factorial(n) / (2*(factorial(n-2)))
        num_pairs += combinations
    if num_pairs > max_pairs:
        max_pairs = num_pairs
print (int(max_pairs))