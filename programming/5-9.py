n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
count = 0
for i in range(n):
    row_max = max(matrix[i])
    for j in range(n):
        if matrix[i][j] == row_max:
            col_min = matrix[i][j]
            is_point = True
            for k in range(n):
                if matrix[k][j] < col_min:
                    is_point = False
                    break
            if is_point:
                count += 1
print(count)