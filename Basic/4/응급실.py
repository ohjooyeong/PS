# 응급실

from collections import deque

n, m = map(int, input().split())

arr = list(map(int, input().split()))
dq = deque()

for i in range(n):
    dq.append([arr[i], i])

cnt = 0
while dq:
    p = dq.popleft()
    tmp = 0
    for value in dq:
        if value[0] > tmp:
            tmp = value[0]
    if p[0] >= tmp:
        cnt += 1
        if p[1] == m:
            break
    else:
        dq.append(p)
print(cnt)
