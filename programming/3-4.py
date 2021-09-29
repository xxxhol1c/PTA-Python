chr = input()
str = input()
index = -1
for i in range(0, len(str)):
    if str[i] == chr:
        index = i
if index == -1:
    print('Not Found')
else:
    print(f'index = {index}')   

""" alternative solution
a, b = input(), input()
print("index =", b.rfind(a)) if b.rfind(a) != -1 else print('Not Found')
"""
