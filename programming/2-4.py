a,n=map(int, input().split())   
cur = a
res = a
while n > 1:
    cur = 10 * cur + a
    res = res + cur
    n -= 1
print(f's = {res}') 