n = int(input())
lst = [i for i in range(1, n+1)]
count = 0
while len(lst) > 1:
    for i in lst[:]:
        count += 1
        if count == 3:
            count = 0
            lst.remove(i)
print(lst[0])    
    
