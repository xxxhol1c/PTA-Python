def convert(item, base):
    res = 0
    if isinstance(item, int) or isinstance(item, float):
        res += base
    elif isinstance(item, list):
        for subitem in item:
            res += convert(subitem, base + 1)
    return res

lst = eval(input())
print(convert(lst, 0))