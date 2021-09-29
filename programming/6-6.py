def convert(item, deep, level):
    res = 0 
    if (isinstance(item, int) or isinstance(item, float)) and deep == level:
            res += 1
    elif isinstance(item, list):
        deep += 1
        for subitem in item:  
            res += convert(subitem, deep, level)
    return res

lst = eval(input())
n = int(input())
print(convert(lst, 0, n))