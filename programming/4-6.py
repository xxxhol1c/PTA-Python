""" timeout
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2) """

def fib(n):
    pre , cur = 0, 1
    for _ in range(1, n):
        pre , cur = cur, pre + cur 
    return cur

n = int(input())
if n < 1:
    print('Invalid.')
else:
    for i in range(1, n+1):
        print(f'{fib(i):11}', end='')
        if i % 5 == 0:
            print('')