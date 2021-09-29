str = input().strip()
chr_remove = input().strip()
str =  str.replace(chr_remove.upper(), '').replace(chr_remove.lower(), '')
print(f'result: {str}')
