from math import sqrt

def is_prime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

n = int(input())
for _ in range(n):
    m = int(input())
    if is_prime(m):
        print('Yes')
    else:
        print('No')