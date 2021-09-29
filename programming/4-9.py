print("[1] apple")
print("[2] pear")
print("[3] orange")
print("[4] grape")
print("[0] exit")

price = [0, 3, 2.5, 4.1 ,10.2]
code = list(map(int, input().split()))
count = 0
for i in code:
    if i == 0 or count == 5:
        break
    elif  1 <= i <= 4:
        print(f'price = {price[i]:.2f}')
        
    else:
        print('price = 0.00')
    count += 1
    