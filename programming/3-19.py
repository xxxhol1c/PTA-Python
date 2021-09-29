n = int(input())
lst = [input() for _ in range(n)]
print(f'The longest is: {max(lst, key = len)}')
