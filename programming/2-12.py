from math import sqrt

a, b, c = map(int, input().split())
if (a + b) > c and (a + c) > b and (b + c) > a:
    perimeter = a + b + c 
    s = perimeter / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    print(f'area = {area:.2f}; perimeter = {perimeter:.2f}')
else:
    print('These sides do not correspond to a valid triangle')