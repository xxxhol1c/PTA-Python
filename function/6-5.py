from math import factorial

def funcos(eps, x):
    res, i = 0, 0
    while pow(x, i) / factorial(i) >= eps:
        cur = ((-1)**(i/2)) * pow(x, i) / factorial(i)
        res += cur
        i += 2
    return res


eps = float(input())
x = float(input())
value = funcos(eps, x)
print("cos({0}) = {1:.4f}".format(x, value))