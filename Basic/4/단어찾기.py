# 단어찾기

import collections

n = int(input())

arr = []
for i in range((n + n - 1)):
    arr.append(input())

tmp = collections.Counter(arr)
res = sorted(tmp.items(), key=lambda x: x[1])
print(res[0][0])

# p = dict()
# for i in range(n):
#     word = input()
#     p[word] = 1
# for i in range(n - 1):
#     word = input()
#     p[word] = 0

# for key, val in p.items():
#     if val == 1:
#         print(key)
#         break
