def buildCluster(cluster, node, excluded):
    cluster.append(node)
    excluded.append(node)
    for connection in connects_to[node]:
        if connection not in excluded:
            buildCluster(cluster,connection,excluded)

line = input()
line = line.split(' ')
N = int(line[0])
M = int(line[1])
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

clusters = []
num_clusters = 0
for node in connects_to:
    included = False
    for cluster in clusters:
        if node in cluster:
            included = True
    if included == False:
        cluster = []
        excluded = []
        buildCluster(cluster, node, excluded)
        clusters.append(cluster)
        num_clusters += 1

print (num_clusters)