chr_num = 65
m = int(input())
for i in range(m):
    for j in range(m-i):
        print(chr(chr_num), end = ' ')
        chr_num +=1 
    print()