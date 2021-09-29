n = int(input())
count = 0
sum = 0
for i in range(n):
    dic = eval(input())
    for item in dic:
        path = dic[item]
        for key in path:
            count += 1
            sum += path[key]
print(n, count, sum)