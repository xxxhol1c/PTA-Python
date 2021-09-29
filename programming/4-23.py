m, n = map(int, input().split())
matrix = []
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)
count = 0
for i in range(1,m-1):
	for j in range(1,n-1):
            if matrix[i][j-1] < matrix[i][j] > matrix[i][j+1] and matrix[i-1][j] < matrix[i][j] > matrix[i+1][j]:
                count += 1
                print(f'{matrix[i][j]} {i+1} {j+1}')
if count == 0:
    print("None",m,n)