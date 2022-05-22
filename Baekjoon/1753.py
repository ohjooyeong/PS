# 최단경로 1753
import heapq

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
dis = [INF] * (n + 1)
queue = []


for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

# 다익스트라
# start 에서 각 정점에 대한 거리를 나타내는 함수
# heap으로 푸는 방법
def dijkstra(start):
    dis[start] = 0
    heapq.heappush(queue, [0, start])  # 시작값을 0 으로 초기화

    while queue:
        now_w, now_node = heapq.heappop(queue)

        # 최단 거리가 아닌 경우 스킵
        if dis[now_node] < now_w:
            continue

        for next_node, weight in graph[now_node]:
            next_w = now_w + weight

            # 기존의 최소 가중치 보다 더 작다면 교체한다.
            # 그리고 다음 노드에 다음 가중치를 넣어준다.
            if next_w < dis[next_node]:
                dis[next_node] = next_w
                heapq.heappush(queue, [next_w, next_node])


dijkstra(start)

for i in range(1, n + 1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])


# 다익스트라

# start 에서 각 정점에 대한 거리를 나타내는 함수
# 시간 초과 나는 코드
# visited = [False] * (n + 1)

# def near_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, n + 1):
#         if not visited[i] and dis[i] < min_value:
#             min_value = dis[i]
#             index = i
#     return index


# def dijkstra(start):
#     dis[start] = 0
#     visited[start] = True
#
#     # 시작 노드의 인접한 노드 최단거리 계산
#     for g in graph[start]:
#         dis[g[0]] = g[1]
#
#     # 시작노드 제외 다른 노드 처리
#     for _ in range(n - 1):
#         now = near_smallest_node()
#         visited[now] = True
#         # 해당 노드의 인접한 노드들 간의 거리 계산
#         for next in graph[now]:
#             cost = dis[now] + next[1]
#             if cost < dis[next[0]]:
#                 dis[next[0]] = cost
