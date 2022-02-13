# 양과 늑대 프로그래머스

from collections import defaultdict, deque

wolves = []
dictEdges = defaultdict(list)
max_sheep = 0


def dfs(cur, visited, now_sheep, now_wolf, tour):
    global max_sheep

    if visited[cur]:
        return
    visited[cur] = 1

    if wolves[cur]:
        now_wolf += 1
    else:
        now_sheep += 1
        max_sheep = max(max_sheep, now_sheep)

    if now_wolf >= now_sheep:
        return

    tour += dictEdges[cur]

    for next in tour:
        tour_tmp = []
        for t in tour:
            if t != next:
                tour_tmp.append(t)
        dfs(next, visited[:], now_sheep, now_wolf, tour_tmp)


def solution(info, edges):
    global wolves, dictEdges, max_sheep
    wolves = info
    visited = [0] * len(wolves)

    for e1, e2 in edges:
        dictEdges[e1].append(e2)

    dfs(0, visited, 0, 0, [])

    return max_sheep


# print(
#     solution(
#         [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
#         [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]],
#     )
# )

print(
    solution(
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]],
    )
)
