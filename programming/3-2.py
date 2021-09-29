def is_id (test_lst, weight_lst):
    jud_num = test_lst[-1]
    test = test_lst[:17]
    if test.isdigit():
        sum = 0
        i = 0
        for num in test:
            sum += int(num) * weight_lst[i]
            i += 1
        target = sum % 11
        keys = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        values = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        de =  dict(zip(keys, values))
        if de[target] == jud_num:
            return True
        else:
            return False
    return False

num = int(input())
count = 0
weight_lst = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
for _ in range(num):
    test_lst = input()
    if is_id(test_lst,weight_lst):
        count += 1
    else:
        print(test_lst)
if count == num:
    print('All passed')
