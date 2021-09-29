def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input())
index = 1
while True:
    if fib(index) > n:
        print(fib(index))
        break
    else:
        index += 1
