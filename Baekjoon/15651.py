# N 과 M(3) 15651 백준


def DFS(L):
    if L == m:
        for j in range(m):
            print(res[j], end=" ")
        print()
    else:
        for i in range(1, n + 1):
            res[L] = i
            DFS(L + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * n
    DFS(0)
