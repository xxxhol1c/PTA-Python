lst1 = list(input().split())[1:]
lst2 = list(input().split())[1:]
res = []
for num in lst1:
    if num not in lst2 and num not in res:
        res.append(num)
for num in lst2:
    if num not in lst1 and num not in res:
        res.append(num)
print(' '.join(res))