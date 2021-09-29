n = int(input())
std = []
for _ in range(n):
    std.append(list(input().split()))
std.sort(key = lambda x: int(x[2]) + int(x[3]) + int(x[4]), reverse = True)
print(std[0][1], std[0][0], int(std[0][2]) + int(std[0][3]) + int(std[0][4]))