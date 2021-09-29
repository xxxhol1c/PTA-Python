from math import factorial
n = int(input())
res = 0
for i in range(1,n+1,2):
    res += factorial(i)
print(f'n={n},s={res}')