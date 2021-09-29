n = int(input())
res = 0
numerator = 2 
denominator = 1
for _ in range(n):
    res += numerator / denominator
    numerator , denominator = numerator + denominator , numerator
print(f'{res:.2f}')