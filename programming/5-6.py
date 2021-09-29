n = int(input())
lst = list(map(int, input().split()))
s = sorted(set(lst))
for i in s:
    print(f'{i}:{lst.count(i)}')