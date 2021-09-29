a,b = map(int, input().split())
count = 0
sum = 0
while a <= b:
    if a < b and count < 5:
        print(f'{a:>5}', end='')
        count += 1
        sum += a
        a += 1
    elif count == 5:
        print('')
        count = 0
    elif a == b:
        print(f'{a:>5}')
        sum += a
        a += 1
print(f'Sum = {sum}')

""" alternative solution 
a,b = map(int,input().split()) 
for i in range(a,b+1): 
   print("%5d"%i,end="" if (i-a+1)%5 and i!=b else "\n" ) 
print("Sum = %d"%((a+b)/2*(b-a+1))) """