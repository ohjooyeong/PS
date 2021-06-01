# 공주구하기

from collections import deque

dq = deque()
n, k = map(int, input().split())
for i in range(1, n + 1):
    dq.append(i)

cnt = 0
while len(dq) > 1:
    cnt += 1
    if cnt == k:
        dq.popleft()
        cnt = 0
    else:
        dq.append(dq.popleft())

print(dq[0])
