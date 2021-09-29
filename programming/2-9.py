lst = list(map(int, input().split()))
lst.sort()
lst = map(str, lst)
print('->'.join(lst))