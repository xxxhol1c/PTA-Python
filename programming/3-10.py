str = input()
count = 0
for chr in str:
    if chr not in 'AEIOU' and  chr.isupper():
        count += 1
print(count)
