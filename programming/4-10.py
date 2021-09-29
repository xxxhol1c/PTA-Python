from math import gcd

m,n = map(int, input().split())
print(gcd(m, n), int(m*n / gcd(m, n)))