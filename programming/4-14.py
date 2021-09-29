letter = blank = digit = other = 0
count = 0
str = input()
while True:
    for item in str:
        count += 1
        if item.isalpha():
            letter += 1
        elif item.isspace():
            blank += 1
        elif item.isdigit():
            digit += 1
        else:
            other += 1
    if count >= 10:
        break
    str = input()
    blank += 1
    count += 1
print(f'letter = {letter}, blank = {blank}, digit = {digit}, other = {other}')
    