def descending_coin(coin): # make the list of coins
    if coin == 5:
        return 2
    elif coin == 2:
        return 1

def partition_coin(change, largest_coin): # make the list of all partition
    if change == 0:
        return [[]]
    elif change < 0 or largest_coin == None:
        return []
    else:
        using_coin = partition_coin(change - largest_coin, largest_coin)
        with_coin = list(map(lambda s: [largest_coin] + s, using_coin))
        without_coin = partition_coin(change, descending_coin(largest_coin))
        return with_coin + without_coin

change = int(input())
lst = partition_coin(change, 5)
lst_iter = lst[:]  # make the copy to avoid iterative error

for item in lst_iter:  # filter the partition
    if item.count(1) == 0 or item.count(2) ==0 or item.count(5) ==0:
        lst.remove(item)

for item in lst:
    print(f'fen5:{item.count(5)}, fen2:{item.count(2)}, fen1:{item.count(1)}, total:{len(item)}')
print(f'count = {len(lst)}')