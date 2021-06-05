# 아나그램

import collections

a = input()
b = input()

a = dict(collections.Counter(a))
b = dict(collections.Counter(b))

for i in a:
    if a[i] != b[i]:
        print("NO")
        break
else:
    print("YES")
