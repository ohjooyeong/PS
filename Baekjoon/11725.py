# 트리의 부모 찾기 11725

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]

# 트리 연결
for i in range(n - 1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

q = deque()
q.append(1)
visited = [False for _ in range(n + 1)]  # 방문 확인
res = [0 for _ in range(n + 1)]  # 결과

while q:
    now = q.popleft()  # 현재 가르키는 노드
    for i in tree[now]:  # ex) tree[1] 에 있는 요소를 꺼내면서 tree[1] 에는 4 와 6이 들어있다.
        if not visited[i]:
            res[i] = now
            visited[i] = True
            q.append(i)

for i in range(2, n + 1):
    print(res[i])

print(res)
