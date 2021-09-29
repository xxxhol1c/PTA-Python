from math import sqrt

def prime(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

def PrimeSum(x, y):
    res = 0
    for i in range(x, y+1):
        if prime(i) :
            res += i
    return res

m,n=map(int, input().split())
count = 0
for  i in range(m, n + 1):
    if prime(i):
        count += 1
print(count, PrimeSum(m,n))