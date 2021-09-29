lst = list(map(int, input().split()))
for i in range(0,len(lst),3):
    row= lst[i:i+3]
    for j in row:
        print(f'{j:>4}',  end='')
    print(f'{max(row):>4}{sum(row):>4}')