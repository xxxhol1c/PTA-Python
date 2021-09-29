str1 = input()
chr_16 = '1234567890abcdefABCDEF'
res = ''
for chr in str1:
    if chr in chr_16:
        res += chr
if res == '':
    print('0')
elif '' in str1 and str1.find(res[0])>str1.find('-'):    
    print(-int(res,16))
else:
    print(int(res,16))