str = input()
res = ''
for ch in str:
    if ch.isdigit():
        res += ch
print(int(res))
