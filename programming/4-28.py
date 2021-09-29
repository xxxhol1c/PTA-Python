lst = list(map(int, input().split()))
matrix = []
for i in range(0,len(lst),3):
    matrix.append(lst[i:i+3])
for j in range(3):
    for k in range(3):
        print(f'{matrix[k][j]:>4}', end='')
    print()