m,n = map(int, input().split())
sum = 0
while m <= n:
    sum += ((1 / m) + m**2)
    m += 1
print(f'sum = {sum:.6f}')