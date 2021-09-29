vote=set(input().split(","))
res = []
for i in range(6,11):
    if str(i) not in vote: 
        res.append(str(i))
print(' '.join(res))