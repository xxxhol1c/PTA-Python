lower, upper = map(int, input().split())
if lower > upper:
    print('Invalid.')
else:
    print('fahr celsius')
    while lower <= upper:
        fahr = lower
        celsius = 5 * (fahr - 32) / 9
        print(f'{fahr}{celsius:>6.1f}')
        lower += 2