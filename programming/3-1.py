lst = list(map(int, input().split()))
avg = sum(lst)/len(lst)
for height in lst:
    if height > avg:
        print(height, end=' ')
