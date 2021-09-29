def fib(x):
    if x == 0 or x == 1:
        return 1
    return fib(x-1) + fib(x-2)

def PrintFN(x, y):
    lst = []
    start, end = 0, 0
    while  fib(end) <= y:
        if fib(start) < x:
            start += 1
        if fib(end) <= y:
            end += 1

    for num in range(start, end):
        lst.append(fib(num))
    return lst


m,n,i=input().split()
n=int(n)
m=int(m)
i=int(i)
b=fib(i)
print("fib({0}) = {1}".format(i,b))
fiblist=PrintFN(m,n)
print(len(fiblist))