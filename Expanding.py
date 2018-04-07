import itertools

def testValid(combo,pairs):
    combinations = list(itertools.combinations(combo,2))
    for pair in combinations:
        if pair in pairs:
            return False
    return True

line = input()
line = line.split(' ')
N = int(line[0])
M = int(line[1])
pairs = []
for i in range(M):
    line = input()
    line = line.split()
    inp = int(line[0])
    out = int(line[1])
    pairs.append((inp,out))

max = 0
original = [i for i in range(N)]
found = False
n = N
if n > 100:
    n = n - 20
while found == False:
    n -= 1
    combinations = list(itertools.combinations(original,n))
    for combo in combinations:
        valid = testValid(combo,pairs)
        if valid == True:
            found = True
            break

print (n)