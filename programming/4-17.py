n = int(input())
for i in range(10**(n-1), 10**n):
    if i == sum([int(num)**n for num in str(i)]):
        print(i)