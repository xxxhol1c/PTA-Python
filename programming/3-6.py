lst = list(map(int, input().split()))
count = 0
lst = lst[1:]
for num in lst:
    if lst.count(num) > count:
        count = lst.count(num)
        res = num
print(f'{res} {count}')