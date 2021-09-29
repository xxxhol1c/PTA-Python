n = int(input())
if n == 0:
    print('average = 0.0\ncount = 0')
else:
    lst = list(map(int, input().split()))
    count = list(filter(lambda x: x >= 60, lst))
    print(f'average = {sum(lst)/n:.1f}')
    print(f'count = {len(count)}')

