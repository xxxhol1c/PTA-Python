str = input()
res = ''
for chr in str:
    if chr.isalpha() and chr.upper() not in res.upper():
        res +=  chr
if len(res) < 10:
    print('not found')
else:
    print(res[:10])
