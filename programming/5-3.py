x = eval(input())
operator = input() 
y = eval(input())

try:
    dic = {"+": x+y, "-": x-y, "*": x*y, "/": x/y}
    print(f'{dic[operator]:.2f}')

except:
    print('divided by zero')