from math import factorial

error = float(input())
res = 0
i = 0
while True:
    res += 1/factorial(i)
    if 1/factorial(i+1) <= error:
        res += 1/factorial(i+1)
        break
    else:
        i += 1
print(f'{res:.6f}')