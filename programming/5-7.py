lst = eval(input())
res = []
for i in lst:
    if str(i) not in res:
        res.append(str(i))
print(' '.join(res))