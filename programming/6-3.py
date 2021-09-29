def convert(item):
    res = 0
    if isinstance(item, int) or isinstance(item, float):
        res += item
    elif isinstance(item, list) or isinstance(item, tuple):
        for subitem in item:
            res += convert(subitem)
    return res

n = eval(input())
print(convert(n))