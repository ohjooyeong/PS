# N 과 M(2) 15650 백준


def DFS(L, s):
    if L == m:
        for j in range(m):
            print(res[j], end=" ")
        print()
    else:
        for i in range(s, n + 1):
            res[L] = i
            DFS(L + 1, 1 + i)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * n
    DFS(0, 1)
