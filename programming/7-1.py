import re
import sys
import collections
text = sys.stdin.read()
text = text[:text.find('#')]
text = text.lower()
words = re.findall(r'\w+', text)
words = [word if len(word) <= 15 else word[:15] for word in words]
count = collections.Counter(words)
res = sorted(count.items(), key=lambda x: (-x[1], x[0]))
print(len(res))
for i in range(int(0.1*len(res))):
    print(f'{res[i][1]}:{res[i][0]}')