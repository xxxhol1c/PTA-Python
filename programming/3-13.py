str = input()
res = ''
for char in str:
    if char.isupper():
        res += chr(155 - ord(char))
    else:
        res += char
print(res)