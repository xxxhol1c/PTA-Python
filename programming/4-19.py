n = int(input())
total = 0
for i in range(n):
    lst = list(map(int, input().split()))
    if i == n - 1:
        break
    else:
        lst.pop(-i-1)
        if i > 0:
            lst.pop(-1)
        total += sum(lst)
print(total)