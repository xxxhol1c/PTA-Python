from math import sqrt

def is_perfect(num):
    if sum(factor(num)) == num:
        return True
    return False
    
    
def factor(num):
    res = [1]
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            res.append(i)
            if i*i != num:
                res.append(num//i)
    res.sort()
    return res

m, n = map(int, (input().split()))
count = 0
for i in range(m, n+1):
    if is_perfect(i):
        count += 1
        print(f'{i} = ',end='')
        print(' + '.join(list(map(str, factor(i)))))
if count == 0:
    print('None')