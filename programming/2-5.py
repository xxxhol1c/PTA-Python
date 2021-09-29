n = int(input())
sum = 0
for i in range(0, n):
    sum += 1 / (2 * i + 1)
print(f'sum = {sum:.6f}')