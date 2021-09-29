dic1 = eval(input())
dic2 = eval(input())
dic3 = {}
for i in dic1:
    dic3[i] = dic1[i] + dic2.get(i,0)  # to avoid nontype, default = 0
for i in dic2:
    if i not in dic3:
        dic3[i]=dic2[i]
dic3 = dict(sorted(dic3.items(), key=lambda x: x[0] if type(x[0])==int else ord(x[0])))

count = 0
print('{',end='')

for i in dic3:
    if type(i) == str:
        print(f'"{i}":{dic3[i]}', end='')
    else:
        print(f'{i}:{dic3[i]}', end='')
    count +=1
    if count != len(dic3):
        print(',',end='')

print('}')
