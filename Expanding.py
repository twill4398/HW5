from math import factorial

line = input()
line = line.split(' ')
N = int(line[0])
M = int(line[1])
pairs = []
connects_to = {}
for i in range(M):
    line = input()
    line = line.split()
    inp = int(line[0])
    out = int(line[1])
    pairs.append((inp,out))
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
for pair in pairs:
    reachable_nodes = []
    num_pairs = 0
    inp = pair[0]
    out = pair[1]
    for element in pair:
        reachable_nodes.append(element)
    try:
        for element in connects_to[inp]:
            if element not in reachable_nodes:
                reachable_nodes.append(element)
    except KeyError:
        pass
    try:
        for element in connects_to[out]:
            if element not in reachable_nodes:
                reachable_nodes.append(element)
    except KeyError:
        pass
    n = len(reachable_nodes)
    num_pairs = n * ((n-1) /2)
    if num_pairs > max_pairs:
        max_pairs = num_pairs
print (int(max_pairs))