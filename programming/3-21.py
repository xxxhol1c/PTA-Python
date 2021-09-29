str = input()
res = True
for i in range(len(str)):
    if str[i] != str[len(str) - 1 - i]:
        res = False
        break
if res:
    print(str)
    print('Yes')
else:
    print(str)
    print('No')
    
