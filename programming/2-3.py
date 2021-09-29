n = int(input())
if n <= 0:
    print('Invalid Value!')
elif n <= 50:
    cost = 0.53 * n
    print(f'cost = {cost:.2f}')
else:
    cost = 26.5 + 0.58 * (n - 50)
    print(f'cost = {cost:.2f}')