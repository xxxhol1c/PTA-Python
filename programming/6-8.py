def permutations(seq):
    res = []
    if len(seq) == 1:
        return [seq]
    for perm in permutations(seq[1:]):
        for i in range(len(seq)):
            res.append(perm[:i] + str(seq[0])+ perm[i:])
    return res

n = int(input())
seq = ''
for i in range(1,n+1):
    seq += str(i)
lst = list(map(int, permutations(seq)))
lst.sort()
for num in lst:
    print(num)