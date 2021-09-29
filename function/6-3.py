def CountDigit(n,d):
    n = abs(n)
    times = 0
    while n > 0:
        if n % 10 == d:
            times += 1
        n = n // 10
    return times

number,digit=input().split()
number=int(number)
digit=int(digit)
count=CountDigit(number,digit)
print("Number of digit 2 in "+str(number)+":",count)