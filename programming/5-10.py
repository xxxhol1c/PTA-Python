lst = list(map(int, input().split(',')))
n = int(input())
dic = {}
for i in lst:
    dic[i] = n - i
for num in lst:
    if n - num in dic:
        print(f'{lst.index(num)} {lst.index(n-num)}')
        break
else:
    print('no answer')