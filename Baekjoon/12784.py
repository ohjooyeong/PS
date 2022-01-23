# 인하니카 공화국 12784
import sys, math

input = sys.stdin.readline
T = int(input())


def dfs(now, dist):
    global island, tree
    ret, child, check = dist, 0, 0
    island[now] = 1
    for i in range(len(tree[now])):
        if island[tree[now][i][0]] == 0:
            child += dfs(tree[now][i][0], tree[now][i][1])
            check = 1
    if check == 0:
        return ret
    ret = min(ret, child)
    return ret


for _ in range(T):
    x, y = map(int, input().split())
    inf = math.inf

    tree = [[] for _ in range(x + 1)]
    island = [0] * 1001

    # 트리 연결
    for i in range(y):
        a, b, v = map(int, input().split())
        tree[a].append([b, v])
        tree[b].append([a, v])
    tmp = dfs(1, inf)
    print(tree)
    if tmp == inf:
        print(0)
    else:
        print(tmp)
