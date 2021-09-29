n = int(input())
sum = 0
for i in range(0, n):
    sum += ((-1)**i)*(i + 1) / (2 * i + 1)
print(f'{sum:.3f}')