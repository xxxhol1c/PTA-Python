str = input()
res = ''
for char in str:
    if char.isupper() and char not in res:
        res += char
if res == '':
    print('Not Found')
else:
    print(res)