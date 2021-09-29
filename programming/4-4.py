from math import sqrt

def prime(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

n = int(input())
for i in range(2, n // 2 + 1):
    if prime(i) and prime(n - i):
        print(f'{n} = {i} + {n - i}')
        break