# -*- coding: UTF-8 -*-
import collections

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'c', 'd'])
c2 = collections.Counter({'a': 2, 'b': 3, 'c': 5})
c3 = collections.Counter(a=2, b=3, c=1)

print(c1)
print(c2)
print(c3)

c1.update({'a': 2, 'b': 3, 'c': 5})
print(c1, c1['a'])

for e in c1.elements():
    print(e)
t3c1 = c1.most_common(3)
print(t3c1)


s = 'hello world'
print(collections.Counter(s))

counter2 = collections.defaultdict(int)
for c in s:
    counter2[c] += 1
print(counter2.items())

