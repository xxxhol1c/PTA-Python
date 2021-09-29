def convert(item, weight):
    res = 0
    if isinstance(item, int) or isinstance(item, float):
            res += item * weight
    elif isinstance(item, list):
        for subitem in item:
            res += convert(subitem, weight + 1)
    return res

lst = eval(input())
print(convert(lst, 0))