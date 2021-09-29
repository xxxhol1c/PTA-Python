def acronym(str):
    words = str.split()
    letter = []
    for i in range(len(words)):
        letter += words[i][0].upper()
    return ''.join(letter)

phrase=input()
print(acronym(phrase))