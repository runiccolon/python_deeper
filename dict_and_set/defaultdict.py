import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)
for word in sorted(index, key=str.upper):
    print(word, index[word])


print('*'*20)

ct = collections.Counter('abracadabra')
print(ct)
print(type(ct))
ct.update('aaaaazzz')
print(ct)
print(ct.most_common(2))    # 最常见的n个键和它们的计数
