def fn(x, y):
    cur = x
    res = x
    while y > 1:
        cur = 10 * cur + x
        res = res + cur
        y -= 1
    return res

a,b=input().split()
s=fn(int(a),int(b))
print(s)