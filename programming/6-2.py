n = int(input())
female = []
male = []
stds = [input().split() for i in range(n)]
for std in stds:
    if std[0] == '0':
        female.append(std[1])
    else:
        male.append(std[1])
for i in range(n//2):
    if stds[i][1] in female:
        print(f'{stds[i][1]} {male[-1]}')
        male.remove(male[-1])
    else:
        print(f'{stds[i][1]} {female[-1]}')
        female.remove(female[-1])