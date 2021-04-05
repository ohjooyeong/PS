n, k = map(int, input().split())

tmp = set()

for i in range(1, n // 2):
    if n % i == 0:
        tmp.add(i)
        tmp.add(n // i)
tmp = list(tmp)
if len(tmp) < k:
    print(-1)
else:
    print(tmp[k - 1])

# cnt = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         cnt += 1
#     if cnt == k:
#         print(i)
#         break
# else:
#     print(-1)
