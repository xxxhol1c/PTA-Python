n = int(input())
for i in range(n):
    m = int(input())
    upper_tr = True
    for row in range(m):
        a = list(map(int, input().split()))
        for col in range(row):
            if  a[col] != 0: 
                upper_tr = False
                break
    if upper_tr:
        print("YES")
    else:
        print("NO")
