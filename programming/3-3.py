str = input()
ch1 , ch2 = input().split()
for i in range(len(str)-1, -1, -1):
    if str[i] == ch1 or str[i] == ch2:
        print(f'{i} {str[i]}')